"""
Content Transformer Module

This module transforms extracted documentation into LLM-optimized formats.
"""

import logging
import json
import openai
import os
from tqdm import tqdm

logger = logging.getLogger(__name__)

class Transformer:
    """Class to transform documentation content into LLM-optimized formats."""
    
    def __init__(self, extracted_data, openai_config):
        """
        Initialize with the extracted data.
        
        Args:
            extracted_data (dict): The data from the extraction phase
            openai_config (dict): Configuration for OpenAI API
        """
        self.extracted_data = extracted_data
        self.documents = extracted_data.get("documents", [])
        self.model = openai_config.get("model", "gpt-4")
        
        # Ensure OpenAI API key is set
        self.api_key = os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            logger.warning("OPENAI_API_KEY not found in environment variables")
    
    def transform(self):
        """
        Transform the extracted content into LLM-optimized formats.
        
        Returns:
            dict: Transformed data
        """
        if not self.api_key:
            logger.error("OpenAI API key is required for transformation")
            return self.extracted_data
        
        logger.info(f"Transforming {len(self.documents)} documents using model {self.model}")
        
        transformed_data = {
            "source": self.extracted_data.get("source", ""),
            "description": self.extracted_data.get("description", ""),
            "documents": []
        }
        
        # Set OpenAI API key
        openai.api_key = self.api_key
        
        # Process each document
        for document in tqdm(self.documents, desc="Transforming documents"):
            try:
                transformed_doc = self._transform_document(document)
                transformed_data["documents"].append(transformed_doc)
            except Exception as e:
                logger.error(f"Error transforming document: {e}")
                # Include original document to avoid data loss
                transformed_data["documents"].append(document)
        
        return transformed_data
    
    def _transform_document(self, document):
        """
        Transform a single document.
        
        Args:
            document (dict): The document to transform
            
        Returns:
            dict: Transformed document
        """
        # Create a base transformed document with original fields
        transformed_doc = document.copy()
        
        # Generate an improved summary
        try:
            improved_summary = self._generate_improved_summary(document)
            transformed_doc["improved_summary"] = improved_summary
        except Exception as e:
            logger.error(f"Error generating improved summary: {e}")
            transformed_doc["improved_summary"] = document.get("summary", "")
        
        # Generate question-answer pairs
        try:
            qa_pairs = self._generate_qa_pairs(document)
            transformed_doc["qa_pairs"] = qa_pairs
        except Exception as e:
            logger.error(f"Error generating QA pairs: {e}")
            transformed_doc["qa_pairs"] = []
        
        # Transform sections for better LLM consumption
        try:
            transformed_sections = self._transform_sections(document.get("sections", []))
            transformed_doc["transformed_sections"] = transformed_sections
        except Exception as e:
            logger.error(f"Error transforming sections: {e}")
            transformed_doc["transformed_sections"] = document.get("sections", [])
        
        return transformed_doc
    
    def _generate_improved_summary(self, document):
        """
        Generate an improved summary using OpenAI API.
        
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
        
        # Call OpenAI API
        response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert technical documentation specialist. Your task is to create clear, informative summaries of technical documents that will be easy for language models to understand and use."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.5
        )
        
        # Extract and return the summary
        improved_summary = response.choices[0].message.content.strip()
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
        
        # Call OpenAI API
        response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert in creating educational content. Generate insightful question-answer pairs based on technical documentation."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        # Extract and parse the JSON response
        content = response.choices[0].message.content.strip()
        
        try:
            # Extract JSON from the response content if needed
            if "```json" in content:
                json_content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                json_content = content.split("```")[1].strip()
            else:
                json_content = content
                
            qa_pairs = json.loads(json_content)
            return qa_pairs
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing QA pairs JSON: {e}")
            # Fallback to a simple array if JSON parsing fails
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
        
        for section in sections:
            heading = section.get("heading", "")
            content = section.get("content", "")
            level = section.get("level", 1)
            
            # Skip empty sections
            if not content.strip():
                continue
            
            # Limit content length for API calls
            if len(content) > 2000:
                content = content[:2000] + "..."
            
            prompt = f"""
            Section Heading: {heading}
            
            Original Content:
            {content}
            
            Please transform this section content to be more LLM-friendly by:
            1. Using clear, structured sentences
            2. Organizing information in a logical flow
            3. Removing unnecessary verbosity
            4. Adding contextual information where needed
            5. Maintaining all key technical details
            
            Transformed Content:
            """
            
            try:
                # Call OpenAI API
                response = openai.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are an expert in technical documentation who specializes in creating content optimized for language models."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=max(500, len(content) // 2),
                    temperature=0.4
                )
                
                # Extract the transformed content
                transformed_content = response.choices[0].message.content.strip()
                
                transformed_sections.append({
                    "heading": heading,
                    "level": level,
                    "original_content": content,
                    "transformed_content": transformed_content
                })
                
            except Exception as e:
                logger.error(f"Error transforming section '{heading}': {e}")
                # Include original content if transformation fails
                transformed_sections.append({
                    "heading": heading,
                    "level": level,
                    "original_content": content,
                    "transformed_content": content
                })
        
        return transformed_sections 