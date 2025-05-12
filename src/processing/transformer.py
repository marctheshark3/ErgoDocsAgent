"""
Content Transformer Module

This module transforms extracted documentation into LLM-optimized formats.
"""

import logging
import json
import os
import time
import sys
import traceback
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeRemainingColumn
from rich.console import Console
from rich.panel import Panel

# Import both AI provider SDKs
import openai
import anthropic

logger = logging.getLogger(__name__)

# Create a dedicated logger for API responses
api_logger = logging.getLogger("api_responses")
api_logger.setLevel(logging.DEBUG)
# Create file handler for API responses
api_handler = logging.FileHandler("api_responses.log")
api_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
api_logger.addHandler(api_handler)

class Transformer:
    """Class to transform documentation content into LLM-optimized formats."""
    
    def __init__(self, extracted_data, provider_config, provider_type='openai', console=None):
        """
        Initialize with the extracted data.
        
        Args:
            extracted_data (dict): The data from the extraction phase
            provider_config (dict): Configuration for the AI provider
            provider_type (str): 'openai' or 'anthropic'
            console (Console): Rich console for UI (optional)
        """
        self.extracted_data = extracted_data
        self.documents = extracted_data.get("documents", [])
        self.provider_type = provider_type.lower()
        self.model = provider_config.get("model", self._get_default_model())
        self.console = console or Console()
        self.error_count = 0
        self.max_errors = 3  # Maximum number of errors before stopping
        
        # Store API client/key based on provider type
        if self.provider_type == 'anthropic':
            self.api_key = os.environ.get("ANTHROPIC_API_KEY")
            if self.api_key:
                try:
                    # Initialize Anthropic client without proxies parameter
                    self.client = anthropic.Anthropic(api_key=self.api_key)
                    self.console.print(f"[bold green]✓[/] Anthropic client initialized")
                except Exception as e:
                    self.console.print(f"[bold red]Error initializing Anthropic client: {e}[/]")
                    logger.error(f"Error initializing Anthropic client: {e}")
                    self.client = None
            else:
                self.console.print(f"[bold red]⚠ ANTHROPIC_API_KEY not found in environment variables[/]")
                logger.warning("ANTHROPIC_API_KEY not found in environment variables")
                self.client = None
        else:  # Default to OpenAI
            self.api_key = os.environ.get("OPENAI_API_KEY")
            if not self.api_key:
                self.console.print(f"[bold red]⚠ OPENAI_API_KEY not found in environment variables[/]")
                logger.warning("OPENAI_API_KEY not found in environment variables")
    
    def _get_default_model(self):
        """Get the default model based on provider type"""
        if self.provider_type == 'anthropic':
            return "claude-3-haiku-20240307"
        else:
            return "gpt-3.5-turbo"
    
    def _check_error_threshold(self, error, context=""):
        """Check if we've hit the error threshold and should stop the pipeline"""
        self.error_count += 1
        error_detail = str(error)
        stack_trace = traceback.format_exc()
        
        # Log detailed error information
        logger.error(f"{context}: {error_detail}")
        logger.debug(f"Stack trace: {stack_trace}")
        
        self.console.print(f"[bold red]Error {self.error_count}/{self.max_errors}: {error_detail}[/]")
        
        if self.error_count >= self.max_errors:
            self.console.print(Panel.fit(
                f"[bold red]Stopping pipeline after {self.error_count} errors![/]\n\n"
                f"Last error: {error_detail}\n\n"
                "Please fix the issue before continuing.\n\n"
                "Check api_responses.log for detailed error information.",
                title="[bold red]Error Threshold Reached",
                border_style="red"
            ))
            sys.exit(1)  # Stop the pipeline
    
    def transform(self):
        """
        Transform the extracted content into LLM-optimized formats.
        
        Returns:
            dict: Transformed data
        """
        if not self.api_key:
            self.console.print(f"[bold red]Error: {self.provider_type.upper()} API key is required for transformation[/]")
            logger.error(f"{self.provider_type.upper()} API key is required for transformation")
            return self.extracted_data
        
        document_count = len(self.documents)
        self.console.print(f"[bold blue]Transforming [/][bold yellow]{document_count}[/][bold blue] documents using [/][bold magenta]{self.provider_type}[/][bold blue] model [/][bold green]{self.model}[/]")
        
        transformed_data = {
            "source": self.extracted_data.get("source", ""),
            "description": self.extracted_data.get("description", ""),
            "documents": []
        }
        
        # Set OpenAI API key if using OpenAI
        if self.provider_type == 'openai':
            openai.api_key = self.api_key
        
        # We can't use nested progress bars or status displays when a progress bar is already active
        # Instead, use simple console prints for progress updates
        
        # Document counter for progress reporting
        processed_count = 0
        
        for document in self.documents:
            try:
                title = document.get("title", "Untitled")
                processed_count += 1
                
                # Print progress
                if processed_count % 5 == 0 or processed_count == 1:
                    percent = int((processed_count / document_count) * 100)
                    self.console.print(f"[dim]Processing document {processed_count}/{document_count} ({percent}%) - {title[:40]}...[/]")
                
                # Transform the document (no nested progress bars)
                transformed_doc = self._transform_document(document)
                transformed_data["documents"].append(transformed_doc)
                
            except Exception as e:
                self._check_error_threshold(e, f"Error transforming document '{title}'")
                # Include original document to avoid data loss
                transformed_data["documents"].append(document)
        
        self.console.print(f"[bold green]✓[/] Transformation complete - Processed [bold]{processed_count}[/] documents")
        return transformed_data
    
    def _transform_document(self, document):
        """
        Transform a single document without using progress bars.
        
        Args:
            document (dict): The document to transform
            
        Returns:
            dict: Transformed document
        """
        # Create a base transformed document with original fields
        transformed_doc = document.copy()
        title = document.get("title", "Untitled")
        
        # Generate an improved summary
        try:
            self.console.print(f"[dim]Generating summary for: {title[:40]}...[/]")
            improved_summary = self._generate_improved_summary(document)
            transformed_doc["improved_summary"] = improved_summary
        except Exception as e:
            self._check_error_threshold(e, f"Error generating summary for '{title}'")
            transformed_doc["improved_summary"] = document.get("summary", "")
        
        # Generate question-answer pairs
        try:
            self.console.print(f"[dim]Generating Q&A pairs for: {title[:40]}...[/]")
            qa_pairs = self._generate_qa_pairs(document)
            transformed_doc["qa_pairs"] = qa_pairs
        except Exception as e:
            self._check_error_threshold(e, f"Error generating Q&A pairs for '{title}'")
            transformed_doc["qa_pairs"] = []
        
        # Transform sections for better LLM consumption
        try:
            section_count = len(document.get("sections", []))
            if section_count > 0:
                self.console.print(f"[dim]Processing {section_count} sections for: {title[:40]}...[/]")
            transformed_sections = self._transform_sections(document.get("sections", []))
            transformed_doc["transformed_sections"] = transformed_sections
        except Exception as e:
            self._check_error_threshold(e, f"Error transforming sections for '{title}'")
            transformed_doc["transformed_sections"] = document.get("sections", [])
        
        return transformed_doc
    
    def _generate_improved_summary(self, document):
        """
        Generate an improved summary using AI provider.
        
        Args:
            document (dict): The document data
            
        Returns:
            str: Improved summary
        """
        title = document.get("title", "")
        summary = document.get("summary", "")
        
        # Prepare content for summarization
        sections_text = ""
        for section in document.get("sections", []):
            sections_text += f"\n{section.get('heading', '')}: {section.get('content', '')[:500]}..."
        
        # Limit the sections text
        if len(sections_text) > 4000:
            sections_text = sections_text[:4000] + "..."
        
        prompt = f"""
        Document Title: {title}
        
        Original Summary: {summary}
        
        Content Excerpts: {sections_text}
        
        Please provide a comprehensive, well-structured summary of this document. The summary should:
        1. Capture the key points and concepts
        2. Be optimized for LLM understanding (clear, context-rich language)
        3. Be between 200-300 words
        4. Include relevant technical terminology where appropriate
        
        Summary:
        """
        
        # No status display - just print start/end
        self.console.print(f"[dim]AI: Generating summary...[/]")
        
        if self.provider_type == 'anthropic':
            # Call Anthropic API - no proxies parameter
            try:
                api_logger.info(f"Sending summary generation prompt to Anthropic for document: {title}")
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=500,
                    temperature=0.5,
                    messages=[
                        {"role": "user", "content": "You are an expert technical documentation specialist. Your task is to create clear, informative summaries of technical documents that will be easy for language models to understand and use.\n\n" + prompt}
                    ]
                )
                
                # Log the raw response for debugging
                api_logger.info(f"Anthropic summary response type: {type(response)}")
                
                # Extract the improved summary
                raw_summary = response.content[0].text.strip()
                api_logger.info(f"Document: {title} - Raw Anthropic summary response:\n{raw_summary[:500]}...")
                improved_summary = raw_summary
                
            except Exception as e:
                api_logger.error(f"Anthropic API error during summary generation for document {title}: {str(e)}")
                api_logger.error(f"Stack trace: {traceback.format_exc()}")
                self._check_error_threshold(e, "Anthropic API error in summary generation")
                raise
        else:
            # Call OpenAI API
            try:
                api_logger.info(f"Sending summary generation prompt to OpenAI for document: {title}")
                response = openai.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are an expert technical documentation specialist. Your task is to create clear, informative summaries of technical documents that will be easy for language models to understand and use."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=500,
                    temperature=0.5
                )
                
                # Log the raw response for debugging
                api_logger.info(f"OpenAI summary response type: {type(response)}")
                
                # Extract the improved summary
                raw_summary = response.choices[0].message.content.strip()
                api_logger.info(f"Document: {title} - Raw OpenAI summary response:\n{raw_summary[:500]}...")
                improved_summary = raw_summary
                
            except Exception as e:
                api_logger.error(f"OpenAI API error during summary generation for document {title}: {str(e)}")
                api_logger.error(f"Stack trace: {traceback.format_exc()}")
                self._check_error_threshold(e, "OpenAI API error in summary generation")
                raise
        
        self.console.print(f"[dim]Summary generated (length: {len(improved_summary)} chars)[/]")
        return improved_summary
    
    def _generate_qa_pairs(self, document):
        """
        Generate question-answer pairs from the document.
        
        Args:
            document (dict): The document data
            
        Returns:
            list: List of question-answer pairs
        """
        title = document.get("title", "")
        
        # Collect content from sections
        content = []
        for section in document.get("sections", [])[:5]:  # Limit to first 5 sections
            content.append(f"{section.get('heading', '')}: {section.get('content', '')[:1000]}")
        
        content_text = "\n\n".join(content)
        
        # Limit content length
        if len(content_text) > 4000:
            content_text = content_text[:4000] + "..."
        
        prompt = f"""
        Document Title: {title}
        
        Content:
        {content_text}
        
        Based on the above content, generate 5 question-answer pairs that would be valuable for an LLM to learn from this document. 
        Focus on the key concepts, technical details, and practical applications.
        
        Format your response as a valid JSON array with objects containing 'question' and 'answer' fields. For example:
        [
            {{
                "question": "What is X?",
                "answer": "X is a technology that..."
            }},
            ...
        ]
        """
        
        # No status display - just print start/end
        self.console.print(f"[dim]AI: Generating Q&A pairs...[/]")
        
        raw_response = None
        
        if self.provider_type == 'anthropic':
            # Call Anthropic API - no proxies parameter
            try:
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=1000,
                    temperature=0.7,
                    messages=[
                        {"role": "user", "content": "You are an expert in creating educational content. Generate insightful question-answer pairs based on technical documentation.\n\n" + prompt}
                    ]
                )
                
                # Log the raw response object for debugging
                api_logger.info(f"Anthropic API response object type: {type(response)}")
                api_logger.info(f"Anthropic API response attributes: {dir(response)}")
                
                # Extract content
                raw_response = response.content[0].text.strip()
                api_logger.info(f"Document: {title} - Raw Anthropic response:\n{raw_response}")
                content = raw_response
                
            except Exception as e:
                api_logger.error(f"Anthropic API error for document {title}: {str(e)}")
                self._check_error_threshold(e, "Anthropic API error in QA generation")
                raise
        else:
            # Call OpenAI API
            try:
                response = openai.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are an expert in creating educational content. Generate insightful question-answer pairs based on technical documentation."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=1000,
                    temperature=0.7
                )
                
                # Log the raw response for debugging
                api_logger.info(f"OpenAI API response object type: {type(response)}")
                
                # Extract content
                raw_response = response.choices[0].message.content.strip()
                api_logger.info(f"Document: {title} - Raw OpenAI response:\n{raw_response}")
                content = raw_response
                
            except Exception as e:
                api_logger.error(f"OpenAI API error for document {title}: {str(e)}")
                self._check_error_threshold(e, "OpenAI API error in QA generation")
                raise
        
        try:
            # Log the content we're about to parse as JSON
            api_logger.debug(f"Attempting to parse JSON from:\n{content}")
            
            # Extract JSON from the response content if needed
            if "```json" in content:
                json_content = content.split("```json")[1].split("```")[0].strip()
                api_logger.debug(f"Extracted JSON content from code block:\n{json_content}")
            elif "```" in content:
                json_content = content.split("```")[1].strip()
                api_logger.debug(f"Extracted content from generic code block:\n{json_content}")
            else:
                json_content = content
            
            # Log exact content being passed to json.loads
            api_logger.debug(f"Final JSON string being parsed:\n{repr(json_content)}")
                
            qa_pairs = json.loads(json_content)
            self.console.print(f"[dim]Generated {len(qa_pairs)} Q&A pairs[/]")
            return qa_pairs
            
        except json.JSONDecodeError as e:
            # Log detailed information about the JSON parsing error
            api_logger.error(f"JSON parsing error: {str(e)}")
            api_logger.error(f"Attempted to parse: {repr(json_content)}")
            api_logger.error(f"Error location - Line: {e.lineno}, Column: {e.colno}, Position: {e.pos}")
            
            # If we can extract the problematic line, log it
            if hasattr(e, 'doc') and e.doc:
                lines = e.doc.split('\n')
                if e.lineno - 1 < len(lines):
                    problematic_line = lines[e.lineno - 1]
                    api_logger.error(f"Problematic line: {repr(problematic_line)}")
                    api_logger.error(f"Issue near: {repr(problematic_line[max(0, e.colno - 20):min(len(problematic_line), e.colno + 20)])}")
            
            self._check_error_threshold(e, "Error parsing QA pairs JSON")
            
            # Fallback to a simple array if JSON parsing fails
            self.console.print(f"[yellow]Warning: Failed to parse JSON response. Using fallback Q&A.[/]")
            return [{"question": "What is this document about?", "answer": document.get("summary", "")}]
    
    def _transform_sections(self, sections):
        """
        Transform sections for better LLM consumption.
        
        Args:
            sections (list): List of sections
            
        Returns:
            list: Transformed sections
        """
        transformed_sections = []
        
        if not sections:
            return transformed_sections
        
        # Just use regular iteration without progress bars
        section_count = len(sections)
        
        for i, section in enumerate(sections):
            heading = section.get("heading", "")
            content = section.get("content", "")
            level = section.get("level", 1)
            
            # Skip empty sections
            if not content.strip():
                continue
            
            # Provide occasional progress updates
            if i % 10 == 0 or i == section_count - 1:
                self.console.print(f"[dim]Processing section {i+1}/{section_count}[/]")
            
            # Limit content length for API calls
            if len(content) > 2000:
                content = content[:2000] + "..."
            
            # For now, skip the AI transformation to avoid errors
            # and just use the original content
            transformed_content = content
                
            # Add this section to the results
            transformed_sections.append({
                "heading": heading,
                "level": level,
                "original_content": content,
                "transformed_content": transformed_content
            })
        
        self.console.print(f"[dim]Completed processing {len(transformed_sections)} sections[/]")
        return transformed_sections 