#!/usr/bin/env python3
"""
API Log Analyzer

This script analyzes the api_responses.log file to identify patterns
in failed API responses and provide insights into JSON parsing issues.
"""

import re
import json
import sys
import argparse
from collections import Counter
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

def parse_logs(log_file):
    """Parse the API response log file and extract relevant information."""
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        console.print(f"[bold red]Error: Log file {log_file} not found.[/]")
        return None
    
    # Group log entries together
    entries = []
    current_entry = []
    last_timestamp = None
    
    for line in lines:
        # Check if this is a new log entry (starts with timestamp)
        if re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}', line):
            if current_entry:
                entries.append(current_entry)
                current_entry = []
            current_entry.append(line.strip())
            last_timestamp = line.split(' - ')[0]
        elif last_timestamp and line.strip():
            # Continue previous entry
            current_entry.append(line.strip())
    
    # Add the last entry if there is one
    if current_entry:
        entries.append(current_entry)
    
    return entries

def extract_json_errors(entries):
    """Extract JSON parsing errors from log entries."""
    json_errors = []
    for entry in entries:
        entry_text = ' '.join(entry)
        if 'JSON parsing error' in entry_text:
            error_details = {}
            for line in entry:
                if 'JSON parsing error:' in line:
                    error_details['error'] = line.split('JSON parsing error:')[1].strip()
                elif 'Error location - Line:' in line:
                    match = re.search(r'Line: (\d+), Column: (\d+)', line)
                    if match:
                        error_details['line'] = int(match.group(1))
                        error_details['column'] = int(match.group(2))
                elif 'Problematic line:' in line:
                    error_details['problematic_line'] = line.split('Problematic line:')[1].strip()
                elif 'Attempted to parse:' in line:
                    error_details['attempted_parse'] = line.split('Attempted to parse:')[1].strip()
                elif 'Document:' in line and 'Raw Anthropic response' in line:
                    error_details['document'] = line.split('Document:')[1].split(' - Raw')[0].strip()
                    error_details['provider'] = 'anthropic'
                elif 'Document:' in line and 'Raw OpenAI response' in line:
                    error_details['document'] = line.split('Document:')[1].split(' - Raw')[0].strip()
                    error_details['provider'] = 'openai'
            
            if error_details:
                json_errors.append(error_details)
    
    return json_errors

def analyze_json_errors(json_errors):
    """Analyze patterns in JSON parsing errors."""
    if not json_errors:
        return "No JSON parsing errors found in the logs."
    
    error_types = Counter([e.get('error', 'Unknown error') for e in json_errors])
    providers = Counter([e.get('provider', 'Unknown') for e in json_errors])
    line_numbers = Counter([e.get('line', 0) for e in json_errors if e.get('line')])
    
    # Sample of problematic responses
    sample_errors = json_errors[:3]  # Take first 3 errors as samples
    
    # Analyze for common patterns
    common_patterns = []
    
    # Check for code blocks without proper formatting
    code_block_issues = sum(1 for e in json_errors if "```" in str(e.get('attempted_parse', '')))
    if code_block_issues > 0:
        common_patterns.append(f"Code blocks formatting issues: {code_block_issues} errors")
    
    # Check for truncated responses
    truncated_responses = sum(1 for e in json_errors if len(str(e.get('attempted_parse', ''))) < 20)
    if truncated_responses > 0:
        common_patterns.append(f"Potentially truncated responses: {truncated_responses} errors")
    
    # Check for malformed array brackets
    bracket_issues = sum(1 for e in json_errors if 
                        ('Expecting value' in str(e.get('error', '')) and '[' in str(e.get('problematic_line', ''))) or
                        ('Expecting ]' in str(e.get('error', ''))))
    if bracket_issues > 0:
        common_patterns.append(f"Array bracket issues: {bracket_issues} errors")
    
    # Check for missing commas
    comma_issues = sum(1 for e in json_errors if 'Expecting \',\' delimiter' in str(e.get('error', '')))
    if comma_issues > 0:
        common_patterns.append(f"Missing comma delimiter: {comma_issues} errors")
    
    return {
        "total_errors": len(json_errors),
        "error_types": error_types,
        "providers": providers,
        "line_numbers": line_numbers,
        "sample_errors": sample_errors,
        "common_patterns": common_patterns
    }

def print_analysis(analysis):
    """Print the analysis results in a user-friendly format."""
    if isinstance(analysis, str):
        console.print(Panel.fit(analysis, border_style="yellow"))
        return
    
    console.print(Panel.fit(
        f"[bold green]JSON Parsing Error Analysis[/]",
        border_style="green"
    ))
    
    console.print(f"[bold cyan]Total JSON parsing errors:[/] {analysis['total_errors']}")
    
    # Error types table
    error_table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    error_table.add_column("Error Type")
    error_table.add_column("Count")
    
    for error, count in analysis['error_types'].most_common():
        error_table.add_row(error, str(count))
    
    console.print("\n[bold cyan]Error Types:[/]")
    console.print(error_table)
    
    # Provider table
    provider_table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    provider_table.add_column("Provider")
    provider_table.add_column("Count")
    
    for provider, count in analysis['providers'].most_common():
        provider_table.add_row(provider, str(count))
    
    console.print("\n[bold cyan]Providers:[/]")
    console.print(provider_table)
    
    # Common patterns
    console.print("\n[bold cyan]Common Patterns:[/]")
    if analysis['common_patterns']:
        for pattern in analysis['common_patterns']:
            console.print(f"- {pattern}")
    else:
        console.print("No common patterns identified.")
    
    # Sample errors
    console.print("\n[bold cyan]Sample Error Details:[/]")
    for i, error in enumerate(analysis['sample_errors']):
        console.print(Panel.fit(
            f"[bold]Error {i+1}:[/]\n"
            f"Type: {error.get('error', 'Unknown')}\n"
            f"Provider: {error.get('provider', 'Unknown')}\n"
            f"Document: {error.get('document', 'Unknown')}\n"
            f"Line: {error.get('line', 'Unknown')}, Column: {error.get('column', 'Unknown')}\n\n"
            f"[dim]Problematic line:[/]\n{error.get('problematic_line', 'Not available')}",
            border_style="red"
        ))
    
    # Recommendations
    console.print("\n[bold cyan]Recommendations:[/]")
    if "Expecting value" in str(analysis['error_types']):
        console.print("• Empty or malformed JSON responses - Check if the API responses contain valid JSON")
    if "Expecting ',' delimiter" in str(analysis['error_types']):
        console.print("• Missing commas between array items - Modify prompts to emphasize valid JSON formatting")
    if code_block_issues := any("code block" in p for p in analysis['common_patterns']):
        console.print("• Code block issues - Modify prompts to request raw JSON without markdown formatting")
    if any("Array bracket" in p for p in analysis['common_patterns']):
        console.print("• Array bracket problems - Ensure prompts specify the need for proper [ ] brackets")
    
    console.print("\n[bold cyan]Next Steps:[/]")
    console.print("1. Check the full logs in api_responses.log for detailed response content")
    console.print("2. Modify prompts to be more explicit about JSON formatting requirements")
    console.print("3. Consider adding retry logic with prompt refinement for failed responses")
    console.print("4. Implement client-side JSON validation and repair for common issues")

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Analyze API response logs for JSON parsing issues')
    parser.add_argument('--log', type=str, default='api_responses.log', help='Path to the API response log file')
    args = parser.parse_args()
    
    console.print(Panel.fit(
        "[bold cyan]ErgoDocsAgent[/] - [cyan]API Response Log Analyzer[/]",
        subtitle="[italic]Identifying patterns in API response errors[/]",
        border_style="cyan"
    ))
    
    console.print(f"[bold blue]Analyzing log file: {args.log}[/]")
    entries = parse_logs(args.log)
    
    if not entries:
        console.print("[bold yellow]No log entries found or file is empty.[/]")
        return
    
    console.print(f"[bold green]Found {len(entries)} log entries[/]")
    
    json_errors = extract_json_errors(entries)
    analysis = analyze_json_errors(json_errors)
    
    print_analysis(analysis)

if __name__ == "__main__":
    main() 