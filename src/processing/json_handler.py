"""
JSON Response Handler

This module provides utility functions for handling JSON responses from LLMs,
including parsing, validation, and error recovery.
"""

import json
import re
import logging

# Set up dedicated logger for JSON processing
logger = logging.getLogger("json_handler")

def extract_json_from_text(text):
    """
    Extract JSON content from text that may contain other content.
    
    Args:
        text (str): Text that may contain JSON
        
    Returns:
        str: Extracted JSON string or original text if no JSON markers found
    """
    # First check for explicit code blocks with JSON
    if "```json" in text:
        # Extract content between ```json and the next ```
        match = re.search(r'```json\s*([\s\S]*?)\s*```', text)
        if match:
            return match.group(1).strip()
    
    # Check for any code block
    if "```" in text:
        # Extract content between any ``` markers
        match = re.search(r'```\s*([\s\S]*?)\s*```', text)
        if match:
            return match.group(1).strip()
    
    # Check for JSON array or object at the start
    match = re.search(r'(\[|\{)[\s\S]*?(\]|\})', text)
    if match and match.start() < 10:  # Only if it starts near the beginning
        # Get the full JSON string
        json_str = text[match.start():match.end()]
        return json_str
    
    # If no JSON markers found, return the original text
    return text

def clean_json_string(json_str):
    """
    Clean a JSON string by fixing common issues that cause parsing errors.
    
    Args:
        json_str (str): JSON string to clean
        
    Returns:
        str: Cleaned JSON string
    """
    # Remove any text before the first [ or {
    first_bracket = min(
        json_str.find('[') if json_str.find('[') != -1 else float('inf'),
        json_str.find('{') if json_str.find('{') != -1 else float('inf')
    )
    if first_bracket != float('inf'):
        json_str = json_str[first_bracket:]
    
    # Remove any text after the last matching ] or }
    last_square_bracket = json_str.rfind(']')
    last_curly_bracket = json_str.rfind('}')
    
    if last_square_bracket != -1 and (last_curly_bracket == -1 or last_square_bracket > last_curly_bracket):
        json_str = json_str[:last_square_bracket + 1]
    elif last_curly_bracket != -1:
        json_str = json_str[:last_curly_bracket + 1]
    
    # Fix common escape sequence issues
    json_str = json_str.replace('\n', '\\n')
    json_str = json_str.replace('\t', '\\t')
    
    # Fix control characters
    json_str = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', json_str)
    
    # Fix unescaped quotes in strings
    json_str = re.sub(r'(?<!\\)"(?=.*?[^\\]")', '\\"', json_str)
    
    return json_str

def parse_json_safely(text, default_value=None):
    """
    Safely parse JSON content from text with several fallback mechanisms.
    
    Args:
        text (str): Text containing JSON
        default_value: Value to return if parsing fails
        
    Returns:
        object: Parsed JSON object or default_value if parsing fails
    """
    if not text or not text.strip():
        logger.warning("Empty text provided for JSON parsing")
        return default_value
    
    try:
        # First try direct parsing
        return json.loads(text)
    except json.JSONDecodeError as e:
        # Log the initial error
        logger.warning(f"Initial JSON parsing failed: {str(e)}")
        
        # Try extracting JSON from text
        json_str = extract_json_from_text(text)
        if json_str != text:
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                # Extraction didn't help, continue to cleaning
                pass
        
        # Try cleaning the JSON string
        cleaned_json = clean_json_string(json_str)
        if cleaned_json != json_str:
            try:
                return json.loads(cleaned_json)
            except json.JSONDecodeError as e:
                # Log the error with detailed information
                logger.error(f"JSON parsing error after cleaning: {str(e)}")
                logger.error(f"Attempted to parse: {repr(cleaned_json)}")
                
                # Try to fix the specific error location
                if hasattr(e, 'pos'):
                    fixed_json = fix_json_at_position(cleaned_json, e.pos)
                    try:
                        return json.loads(fixed_json)
                    except:
                        pass
    
    # If all attempts fail, return the default value
    return default_value

def fix_json_at_position(json_str, error_position):
    """
    Attempt to fix JSON at a specific error position.
    
    Args:
        json_str (str): JSON string with error
        error_position (int): Position of the error
        
    Returns:
        str: Potentially fixed JSON string
    """
    # Simple fix: if error is at a quote, try escaping it
    if error_position > 0 and error_position < len(json_str):
        if json_str[error_position] == '"' and json_str[error_position - 1] != '\\':
            return json_str[:error_position] + '\\' + json_str[error_position:]
    
    # More fixes could be implemented here
    return json_str

def validate_qa_pairs(qa_pairs, min_pairs=1, max_pairs=10):
    """
    Validate question-answer pairs and fix common issues.
    
    Args:
        qa_pairs (list): List of question-answer pairs
        min_pairs (int): Minimum number of pairs required
        max_pairs (int): Maximum number of pairs allowed
        
    Returns:
        list: Validated and fixed question-answer pairs
    """
    # If qa_pairs is None or not a list, return an empty list
    if not qa_pairs or not isinstance(qa_pairs, list):
        logger.warning("Invalid QA pairs: not a list")
        return []
    
    # Validate each pair
    valid_pairs = []
    for i, pair in enumerate(qa_pairs):
        if isinstance(pair, dict):
            # Get question and answer, defaulting to empty strings
            question = pair.get("question", "")
            answer = pair.get("answer", "")
            
            # Skip if either question or answer is missing
            if not question or not answer:
                logger.warning(f"Skipping QA pair {i}: missing question or answer")
                continue
            
            # Clean up question and answer
            question = question.strip()
            answer = answer.strip()
            
            # Add valid pair
            valid_pairs.append({"question": question, "answer": answer})
        else:
            logger.warning(f"Skipping QA pair {i}: not a dictionary")
    
    # Ensure minimum number of pairs
    if len(valid_pairs) < min_pairs:
        logger.warning(f"Only {len(valid_pairs)} valid QA pairs found, minimum {min_pairs} required")
    
    # Limit to maximum number of pairs
    if len(valid_pairs) > max_pairs:
        logger.warning(f"Limiting QA pairs from {len(valid_pairs)} to {max_pairs}")
        valid_pairs = valid_pairs[:max_pairs]
    
    return valid_pairs

def format_qa_pairs_for_prompt():
    """
    Get a template string for properly formatting QA pairs in a prompt.
    
    Returns:
        str: Template for QA pairs format
    """
    return """
Please respond with ONLY a valid JSON array of question-answer pairs in this exact format:

[
    {
        "question": "First question here?",
        "answer": "First answer here."
    },
    {
        "question": "Second question here?",
        "answer": "Second answer here."
    }
]

Do not include any text before or after the JSON.
Do not include ```json or ``` markers.
Do not include any explanations.
"""

def format_for_summary_prompt():
    """
    Get a template string for properly formatting summary in a prompt.
    
    Returns:
        str: Template for summary format
    """
    return """
Please respond with ONLY the summary text, without any prefixes like "Summary:" or explanations.
The summary should be concise and cover the key points from the document.
Do not include any JSON formatting or markdown annotations.
""" 