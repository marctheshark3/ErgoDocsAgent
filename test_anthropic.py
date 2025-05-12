#!/usr/bin/env python3
"""
Simple test script to verify Anthropic API connectivity and Claude model availability
"""

import os
import sys
import json
import logging
import anthropic
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("anthropic_test")

def load_config():
    """Load model configuration from config.json"""
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
        return config.get('ai', {}).get('anthropic', {}).get('model', 'claude-3-haiku-20240307')
    except Exception as e:
        logger.error(f"Error loading config.json: {e}")
        return 'claude-3-haiku-20240307'  # Default fallback

def test_anthropic_connectivity():
    """Test basic Anthropic API connectivity and model availability"""
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        logger.error("ANTHROPIC_API_KEY not found in environment variables")
        return False
    
    # Get configured model
    configured_model = load_config()
    logger.info(f"Using model from config: {configured_model}")
    
    # Test model specified in config.json
    try:
        # Initialize Anthropic client
        client = anthropic.Anthropic(api_key=api_key)
        logger.info("Successfully initialized Anthropic client")
        
        # Anthropic doesn't have a list models endpoint, so we'll just use the configured model
        # and handle any errors that occur
        logger.info(f"Using configured model: {configured_model}")
        
        # Test a simple message
        logger.info(f"Testing simple message with {configured_model}...")
        response = client.messages.create(
            model=configured_model,
            max_tokens=10,
            messages=[
                {"role": "user", "content": "Say hello world!"}
            ]
        )
        
        logger.info(f"Received response: {response.content[0].text}")
        logger.info("Anthropic API test successful!")
        
        return True
    
    except anthropic.APIError as e:
        logger.error(f"Anthropic API error: {e}")
        return False
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_anthropic_connectivity()
    if not success:
        logger.error("Anthropic API test failed! Check your API key and permissions.")
        sys.exit(1)
    else:
        logger.info("All tests passed!")
        sys.exit(0) 