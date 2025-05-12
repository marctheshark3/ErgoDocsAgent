#!/usr/bin/env python3
"""
Test script to verify Anthropic client initialization with proper error handling
"""

import os
import sys
import logging
import anthropic
from dotenv import load_dotenv
from rich.console import Console

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("anthropic_test")
console = Console()

def test_anthropic_client():
    """Test Anthropic client initialization and simple API call"""
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[bold red]ANTHROPIC_API_KEY not found in environment variables[/]")
        return False
    
    try:
        # Initialize Anthropic client - no proxies
        console.print("[bold yellow]Initializing Anthropic client...[/]")
        client = anthropic.Anthropic(api_key=api_key)
        console.print("[bold green]✓ Successfully initialized Anthropic client[/]")
        
        # Test a simple message
        console.print("[bold yellow]Testing simple API call with claude-3-haiku...[/]")
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=10,
            messages=[
                {"role": "user", "content": "Say hello world!"}
            ]
        )
        
        console.print(f"[bold green]✓ Received response: {response.content[0].text}[/]")
        console.print("[bold green]Anthropic client test successful![/]")
        
        return True
    
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/]")
        console.print(f"[bold yellow]Error type: {type(e).__name__}[/]")
        return False

if __name__ == "__main__":
    console.print("\n[bold cyan]Testing Anthropic Client Initialization[/]\n")
    success = test_anthropic_client()
    if not success:
        console.print("[bold red]Anthropic client test failed![/]")
        sys.exit(1)
    else:
        console.print("[bold green]All tests passed![/]")
        sys.exit(0) 