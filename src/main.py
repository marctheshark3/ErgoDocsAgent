#!/usr/bin/env python3
"""
ErgoDocsAgent - Documentation Processing AI Agent

This script ingests documentation from various sources, processes it,
and generates LLM-optimized documentation files.
"""

import os
import json
import logging
import argparse
import time
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

# Import our new pipeline
from src.utils.pipeline import DocumentPipeline

# Initialize Rich console
console = Console()

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ergo_docs_agent.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def load_config(config_path):
    """Load the configuration file."""
    try:
        console.print(f"[bold blue]Loading configuration from {config_path}...[/]")
        with open(config_path, 'r') as f:
            config = json.load(f)
        console.print(f"[bold green]✓[/] Configuration loaded successfully")
        return config
    except Exception as e:
        console.print(f"[bold red]Error loading config file: {e}[/]")
        logger.error(f"Error loading config file: {e}")
        raise

def run_pipeline(config, source_override=None):
    """Run the complete documentation processing pipeline."""
    console.print(Panel.fit(
        "[bold cyan]ErgoDocsAgent[/] - Documentation Processing Pipeline", 
        border_style="cyan"
    ))
    
    # Initialize the new pipeline
    pipeline = DocumentPipeline(config, console=console)
    
    # Run the pipeline and get statistics
    start_time = time.time()
    stats = pipeline.run(source_override)
    duration = time.time() - start_time
    
    # Check for errors
    if "error" in stats:
        console.print(f"[bold red]Error: {stats['error']}[/]")
        return
    
    # Display statistics table
    table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column("Source")
    table.add_column("Documents")
    table.add_column("New")
    table.add_column("Updated")
    table.add_column("Unchanged")
    table.add_column("Errors")
    table.add_column("Status")
    
    for source_stat in stats["sources"]:
        table.add_row(
            source_stat["name"],
            str(source_stat.get("total_documents", 0)),
            str(source_stat.get("new_documents", 0)),
            str(source_stat.get("updated_documents", 0)),
            str(source_stat.get("unchanged_documents", 0)),
            str(source_stat.get("errors", 0)),
            "[bold green]COMPLETE[/]" if source_stat.get("status") == "COMPLETE" else "[bold red]FAILED[/]"
        )
    
    console.print("\n[bold cyan]Pipeline Summary[/]")
    console.print(table)
    
    # Display overall summary
    console.print(Panel.fit(
        f"[bold green]Documentation processing completed in {duration:.2f} seconds[/]\n"
        f"[white]Total documents: {stats['total_documents']}[/]\n"
        f"[white]New documents: {stats['new_documents']}[/]\n"
        f"[white]Updated documents: {stats['updated_documents']}[/]\n"
        f"[white]Unchanged documents: {stats['unchanged_documents']}[/]\n"
        f"[white]Errors: {stats['errors']}[/]", 
        border_style="green"
    ))

def clear_fingerprints(config):
    """Clear all document fingerprints to force fresh processing."""
    console.print("[bold yellow]Clearing document fingerprints...[/]")
    
    # Initialize the pipeline to use its clear_fingerprints method
    pipeline = DocumentPipeline(config, console=console)
    count = pipeline.clear_fingerprints()
    
    console.print(Panel.fit(
        f"[bold green]Removed {count} fingerprint files[/]\n"
        "[white]Next pipeline run will process all documents as new.[/]",
        border_style="green"
    ))

def main():
    """Main entry point for the script."""
    # Load environment variables
    load_dotenv()
    
    # Print banner
    console.print("\n")
    console.print(Panel.fit(
        "[bold cyan]ErgoDocsAgent[/] - [cyan]Documentation Processing AI Agent[/]",
        subtitle="[italic]Building intelligent documentation from various sources[/]",
        border_style="cyan"
    ))
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='ErgoDocsAgent - Documentation Processing AI Agent')
    parser.add_argument('--config', type=str, default='config.json', help='Path to configuration file')
    parser.add_argument('--source', type=str, help='Process only a specific source URL')
    parser.add_argument('--now', action='store_true', help='Run immediately, then exit')
    parser.add_argument('--force', action='store_true', help='Force reprocessing of all documents, ignoring fingerprints')
    parser.add_argument('--clear-fingerprints', action='store_true', help='Clear all document fingerprints without running the pipeline')
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    # Add force flag to config if specified
    if args.force:
        config['force'] = True
    
    # Check if we should just clear fingerprints
    if args.clear_fingerprints:
        clear_fingerprints(config)
        return
    
    # Run the pipeline
    if args.now or not getattr(args, 'schedule', False):
        run_pipeline(config, args.source)

if __name__ == "__main__":
    main() 