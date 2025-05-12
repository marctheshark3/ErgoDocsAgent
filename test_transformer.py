#!/usr/bin/env python3
"""
Test script for the transformer module
"""

import os
import sys
import json
import logging
from dotenv import load_dotenv

# Add the current directory to Python path
sys.path.insert(0, os.path.abspath('.'))

# Import the transformer module
from src.processing.transformer import Transformer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("transformer_test")

def test_transformer():
    """Test the transformer module with minimal inputs"""
    # Load environment variables
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        logger.error("OPENAI_API_KEY not found in environment variables")
        return False
    
    # Create minimal test data
    test_data = {
        "source": "Test Source",
        "description": "Test Description",
        "documents": [
            {
                "title": "Test Document",
                "summary": "This is a test document for testing the transformer module.",
                "sections": [
                    {
                        "heading": "Test Section 1",
                        "content": "This is the content of test section 1.",
                        "level": 1
                    },
                    {
                        "heading": "Test Section 2",
                        "content": "This is the content of test section 2.",
                        "level": 2
                    }
                ]
            }
        ]
    }
    
    # Create a test configuration with various models to try
    models_to_try = ["gpt-3.5-turbo", "gpt-4-turbo", "gpt-4"]
    
    for model in models_to_try:
        try:
            logger.info(f"Testing transformer with model: {model}")
            
            # Initialize the transformer with the test model
            openai_config = {"model": model}
            transformer = Transformer(test_data, openai_config)
            
            # Test the _generate_improved_summary method first
            logger.info("Testing _generate_improved_summary...")
            summary = transformer._generate_improved_summary(test_data["documents"][0])
            logger.info(f"Generated summary: {summary[:50]}...")
            
            # Test the _generate_qa_pairs method
            logger.info("Testing _generate_qa_pairs...")
            qa_pairs = transformer._generate_qa_pairs(test_data["documents"][0])
            logger.info(f"Generated {len(qa_pairs)} QA pairs")
            
            # Test the _transform_sections method
            logger.info("Testing _transform_sections...")
            sections = transformer._transform_sections(test_data["documents"][0]["sections"])
            logger.info(f"Transformed {len(sections)} sections")
            
            logger.info(f"All transformer tests passed with model {model}!")
            return True
            
        except Exception as e:
            logger.error(f"Error testing transformer with model {model}: {e}")
            logger.info(f"Trying next model...")
    
    logger.error("All models failed. Check API access and permissions.")
    return False

if __name__ == "__main__":
    success = test_transformer()
    if not success:
        logger.error("Transformer test failed!")
        sys.exit(1)
    else:
        logger.info("All tests passed!")
        sys.exit(0) 