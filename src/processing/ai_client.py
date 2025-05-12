"""
AI Client Wrapper

This module provides a unified interface for different AI providers (OpenAI, Anthropic)
with improved error handling and response formatting.
"""

import os
import logging
import time
import traceback

# Import AI provider SDKs
import openai
import anthropic

# Import our JSON handler
from src.processing.json_handler import (
    parse_json_safely,
    validate_qa_pairs,
    format_qa_pairs_for_prompt,
    format_for_summary_prompt
)

# Setup logging
logger = logging.getLogger(__name__)

# Create a dedicated logger for API responses
api_logger = logging.getLogger("api_responses")
api_logger.setLevel(logging.INFO)

class AIClient:
    """Unified AI client for different providers with consistent interfaces"""
    
    def __init__(self, provider_type='openai', model=None, temperature=0.7, max_tokens=1000):
        """
        Initialize the AI client.
        
        Args:
            provider_type (str): 'openai' or 'anthropic'
            model (str): Model name for the specified provider
            temperature (float): Temperature for generations (0.0-1.0)
            max_tokens (int): Maximum tokens to generate
        """
        self.provider_type = provider_type.lower()
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.client = None
        
        # Set default models based on provider
        if self.provider_type == 'anthropic':
            self.model = model or "claude-3-sonnet-20240229"
            self._init_anthropic()
        else:  # default to OpenAI
            self.provider_type = 'openai'  # normalize
            self.model = model or "gpt-4"
            self._init_openai()
    
    def _init_anthropic(self):
        """Initialize the Anthropic client"""
        self.api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            logger.error("ANTHROPIC_API_KEY not found in environment variables")
            return
        
        try:
            self.client = anthropic.Anthropic(api_key=self.api_key)
            logger.info("Anthropic client initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing Anthropic client: {str(e)}")
            self.client = None
    
    def _init_openai(self):
        """Initialize the OpenAI client"""
        self.api_key = os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            logger.error("OPENAI_API_KEY not found in environment variables")
            return
        
        openai.api_key = self.api_key
        self.client = openai  # Use the module as the client
        logger.info("OpenAI client initialized successfully")
    
    def is_ready(self):
        """Check if the client is initialized and ready to use"""
        if self.provider_type == 'anthropic':
            return self.client is not None
        else:
            return self.api_key is not None
    
    def generate_summary(self, document, retries=2):
        """
        Generate a summary for a document.
        
        Args:
            document (dict): Document data including title and content
            retries (int): Number of retries for API failures
            
        Returns:
            str: Generated summary
        """
        if not self.is_ready():
            logger.error(f"{self.provider_type.upper()} client not initialized")
            return ""
        
        # Extract document information
        title = document.get("title", "Untitled")
        
        # Collect content from sections
        content = []
        for section in document.get("sections", [])[:10]:  # Limit to first 10 sections
            section_text = f"{section.get('heading', '')}: {section.get('content', '')}"
            # Truncate very long sections
            if len(section_text) > 2000:
                section_text = section_text[:2000] + "..."
            content.append(section_text)
        
        content_text = "\n\n".join(content)
        
        # Limit total content length
        if len(content_text) > 8000:
            content_text = content_text[:8000] + "..."
        
        # Create prompt with formatting instructions
        summary_format = format_for_summary_prompt()
        prompt = f"""
        Document Title: {title}
        
        Content:
        {content_text}
        
        Please provide a comprehensive summary of this document.
        {summary_format}
        """
        
        # Log the request
        logger.info(f"Sending summary generation prompt to {self.provider_type.capitalize()} for document: {title}")
        
        # Try to generate with retries
        for attempt in range(retries + 1):
            try:
                if self.provider_type == 'anthropic':
                    response = self.client.messages.create(
                        model=self.model,
                        max_tokens=500,  # Shorter for summaries
                        temperature=0.3,  # Lower for more consistent summaries
                        messages=[
                            {"role": "user", "content": prompt}
                        ]
                    )
                    
                    # Log the response type
                    api_logger.info(f"Anthropic summary response type: {type(response)}")
                    
                    # Extract and log the response content
                    summary = response.content[0].text.strip()
                    api_logger.info(f"Document: {title} - Raw Anthropic summary response:\n{summary[:500]}...")
                    
                else:  # OpenAI
                    response = openai.chat.completions.create(
                        model=self.model,
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant that generates concise document summaries."},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=500,
                        temperature=0.3
                    )
                    
                    # Extract and log the response content
                    summary = response.choices[0].message.content.strip()
                    api_logger.info(f"Document: {title} - Raw OpenAI summary response:\n{summary[:500]}...")
                
                return summary
                
            except Exception as e:
                logger.error(f"{self.provider_type.capitalize()} API error in attempt {attempt+1}/{retries+1}: {str(e)}")
                if attempt < retries:
                    # Wait before retrying (exponential backoff)
                    time.sleep(2 ** attempt)
                else:
                    # Log the full traceback on final attempt
                    logger.error(f"Traceback: {traceback.format_exc()}")
                    return ""
    
    def generate_qa_pairs(self, document, retries=2):
        """
        Generate question-answer pairs for a document.
        
        Args:
            document (dict): Document data including title and content
            retries (int): Number of retries for API failures
            
        Returns:
            list: List of question-answer pairs
        """
        if not self.is_ready():
            logger.error(f"{self.provider_type.upper()} client not initialized")
            return []
        
        # Extract document information
        title = document.get("title", "Untitled")
        
        # Collect content from sections
        content = []
        for section in document.get("sections", [])[:5]:  # Limit to first 5 sections
            section_text = f"{section.get('heading', '')}: {section.get('content', '')}"
            # Truncate very long sections
            if len(section_text) > 1500:
                section_text = section_text[:1500] + "..."
            content.append(section_text)
        
        content_text = "\n\n".join(content)
        
        # Limit total content length
        if len(content_text) > 6000:
            content_text = content_text[:6000] + "..."
        
        # Create prompt with formatting instructions
        qa_format = format_qa_pairs_for_prompt()
        prompt = f"""
        Document Title: {title}
        
        Content:
        {content_text}
        
        Based on the above content, generate 5 question-answer pairs that would be valuable for an LLM to learn from this document.
        Focus on the key concepts, technical details, and practical applications.
        
        {qa_format}
        """
        
        # Log the request
        logger.info(f"Sending QA generation prompt to {self.provider_type.capitalize()} for document: {title}")
        
        # Try to generate with retries
        for attempt in range(retries + 1):
            try:
                if self.provider_type == 'anthropic':
                    response = self.client.messages.create(
                        model=self.model,
                        max_tokens=self.max_tokens,
                        temperature=self.temperature,
                        system="You are an expert in creating educational content. Generate JSON-formatted question-answer pairs with no other text.",
                        messages=[
                            {"role": "user", "content": prompt}
                        ]
                    )
                    
                    # Log the response type
                    api_logger.info(f"Anthropic API response object type: {type(response)}")
                    api_logger.info(f"Anthropic API response attributes: {dir(response)}")
                    
                    # Extract the content
                    raw_response = response.content[0].text.strip()
                    api_logger.info(f"Document: {title} - Raw Anthropic response:\n{raw_response}")
                    
                else:  # OpenAI
                    response = openai.chat.completions.create(
                        model=self.model,
                        messages=[
                            {"role": "system", "content": "You are an expert in creating educational content. Generate JSON-formatted question-answer pairs with no other text."},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=self.max_tokens,
                        temperature=self.temperature
                    )
                    
                    # Extract the content
                    raw_response = response.choices[0].message.content.strip()
                    api_logger.info(f"Document: {title} - Raw OpenAI response:\n{raw_response}")
                
                # Parse JSON safely using our helper function
                qa_pairs = parse_json_safely(raw_response, [])
                
                # Validate and clean up the QA pairs
                validated_pairs = validate_qa_pairs(qa_pairs)
                
                # Log the final count
                logger.info(f"Generated {len(validated_pairs)} valid QA pairs for document: {title}")
                
                return validated_pairs
                
            except Exception as e:
                logger.error(f"{self.provider_type.capitalize()} API error in attempt {attempt+1}/{retries+1}: {str(e)}")
                if attempt < retries:
                    # Wait before retrying (exponential backoff)
                    time.sleep(2 ** attempt)
                else:
                    # Log the full traceback on final attempt
                    logger.error(f"Traceback: {traceback.format_exc()}")
                    return []
    
    def transform_section(self, section, retries=1):
        """
        Transform a section for better LLM consumption.
        
        Args:
            section (dict): Section data
            retries (int): Number of retries for API failures
            
        Returns:
            str: Transformed section content
        """
        # For now, just return the original content to avoid errors
        # This can be implemented properly later
        return section.get("content", "") 