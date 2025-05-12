#!/usr/bin/env python3
"""
Main test script for AI provider APIs - dynamically selects the appropriate test
based on the default_provider in config.json
"""

import os
import sys
import json
import logging
from dotenv import load_dotenv

# Import test modules
import test_openai
import test_anthropic

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("ai_test")

def load_default_provider():
    """Load default AI provider from config.json"""
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
        return config.get('ai', {}).get('default_provider', 'openai')
    except Exception as e:
        logger.error(f"Error loading config.json: {e}")
        return 'openai'  # Default fallback

def test_api():
    """Run the appropriate test based on the default provider in config"""
    # Load environment variables
    load_dotenv()
    
    # Get default provider
    provider = load_default_provider()
    logger.info(f"Using default provider from config: {provider}")
    
    if provider.lower() == 'openai':
        logger.info("Testing OpenAI API...")
        return test_openai.test_openai_connectivity()
    elif provider.lower() == 'anthropic':
        logger.info("Testing Anthropic API...")
        return test_anthropic.test_anthropic_connectivity()
    else:
        logger.error(f"Unsupported provider: {provider}. Please use 'openai' or 'anthropic'.")
        return False

if __name__ == "__main__":
    success = test_api()
    if not success:
        logger.error("AI API test failed! Check your API key, permissions, and configuration.")
        sys.exit(1)
    else:
        logger.info("All tests passed!")
        sys.exit(0) 