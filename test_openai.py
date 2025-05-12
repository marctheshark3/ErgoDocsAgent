#!/usr/bin/env python3
"""
Simple test script to verify OpenAI API connectivity and model availability
"""

import os
import sys
import json
import logging
import openai
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("openai_test")

def load_config():
    """Load model configuration from config.json"""
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
        return config.get('ai', {}).get('openai', {}).get('model', 'gpt-3.5-turbo')
    except Exception as e:
        logger.error(f"Error loading config.json: {e}")
        return 'gpt-3.5-turbo'  # Default fallback

def test_openai_connectivity():
    """Test basic OpenAI API connectivity and model availability"""
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        logger.error("OPENAI_API_KEY not found in environment variables")
        return False
    
    # Set API key
    openai.api_key = api_key
    
    # Get configured model
    configured_model = load_config()
    logger.info(f"Using model from config: {configured_model}")
    
    # Test model specified in config.json or fallback to GPT-3.5
    try:
        # First get available models
        logger.info("Testing API connectivity and listing available models...")
        models = openai.models.list()
        logger.info(f"Successfully connected to OpenAI API. Found {len(models.data)} models")
        
        # Check available models
        model_names = [model.id for model in models.data]
        logger.info(f"Available model IDs: {', '.join(model_names[:10])}...")
        
        # Check if configured model is available
        if configured_model not in model_names:
            logger.warning(f"Configured model '{configured_model}' not available. Falling back to gpt-3.5-turbo")
            test_model = "gpt-3.5-turbo"
        else:
            logger.info(f"Using configured model: {configured_model}")
            test_model = configured_model
        
        # Test a simple completion
        logger.info(f"Testing simple chat completion with {test_model}...")
        response = openai.chat.completions.create(
            model=test_model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello world!"}
            ],
            max_tokens=10
        )
        
        logger.info(f"Received response: {response.choices[0].message.content}")
        logger.info("OpenAI API test successful!")
        
        return True
    
    except openai.OpenAIError as e:
        logger.error(f"OpenAI API error: {e}")
        return False
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_openai_connectivity()
    if not success:
        logger.error("OpenAI API test failed! Check your API key and permissions.")
        sys.exit(1)
    else:
        logger.info("All tests passed!")
        sys.exit(0) 