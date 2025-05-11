"""
Documentation Generator Module

This module generates output documentation files from processed content.
"""

import os
import logging
import json
import re
from datetime import datetime

logger = logging.getLogger(__name__)

class DocumentationGenerator:
    """Class to generate documentation files from processed content."""
    
    def __init__(self, transformed_data, output_config, source_description):
        """
        Initialize with the transformed data and output configuration.
        
        Args:
            transformed_data (dict): The data from the transformation phase
            output_config (dict): Configuration for output generation
            source_description (str): Description of the source
        """
        self.transformed_data = transformed_data
        self.documents = transformed_data.get("documents", [])
        self.format = output_config.get("format", "markdown")
        self.directory = output_config.get("directory", "output")
        self.structure = output_config.get("structure", "topic")
        self.source_description = source_description
    
    def generate(self):
        """Generate documentation files from the transformed data."""
        logger.info(f"Generating {self.format} documentation in {self.directory}")
        
        # Create output directory if it doesn't exist
        os.makedirs(self.directory, exist_ok=True)
        
        # Generate documentation based on structure
        if self.structure == "topic":
            self._generate_topic_structure()
        elif self.structure == "qa":
            self._generate_qa_structure()
        elif self.structure == "combined":
            self._generate_combined_structure()
        else:
            logger.warning(f"Unknown structure type: {self.structure}, defaulting to topic")
            self._generate_topic_structure()
        
        # Generate metadata file
        self._generate_metadata()
        
        logger.info(f"Documentation generation complete")
    
    def _generate_topic_structure(self):
        """Generate documentation organized by topics/documents."""
        # Create a subdirectory for this source
        source_dir = self._create_source_directory()
        
        # Process each document
        for document in self.documents:
            try:
                title = document.get("title", "Untitled Document")
                
                # Create safe filename
                filename = self._safe_filename(title)
                
                if self.format == "markdown":
                    # Generate markdown file
                    filepath = os.path.join(source_dir, f"{filename}.md")
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(self._generate_markdown_document(document))
                    logger.info(f"Generated {filepath}")
                
                # Generate JSON data file
                json_filepath = os.path.join(source_dir, f"{filename}.json")
                with open(json_filepath, "w", encoding="utf-8") as f:
                    # Create a simplified version for JSON output
                    json_doc = {
                        "title": title,
                        "source_url": document.get("url", document.get("path", "")),
                        "summary": document.get("improved_summary", document.get("summary", "")),
                        "keywords": document.get("keywords", []),
                        "sections": []
                    }
                    
                    # Add transformed sections
                    for section in document.get("transformed_sections", []):
                        json_doc["sections"].append({
                            "heading": section.get("heading", ""),
                            "content": section.get("transformed_content", "")
                        })
                    
                    # Add QA pairs if available
                    if "qa_pairs" in document:
                        json_doc["qa_pairs"] = document.get("qa_pairs", [])
                    
                    json.dump(json_doc, f, indent=2)
                
                logger.info(f"Generated {json_filepath}")
                
            except Exception as e:
                logger.error(f"Error generating document for {document.get('title', 'unknown')}: {e}")
    
    def _generate_qa_structure(self):
        """Generate Q&A format documentation."""
        # Create a subdirectory for this source
        source_dir = self._create_source_directory()
        
        # Create a consolidated QA file
        qa_filename = "question_answer_pairs.md"
        qa_filepath = os.path.join(source_dir, qa_filename)
        
        with open(qa_filepath, "w", encoding="utf-8") as f:
            f.write(f"# Question & Answer Pairs from {self.source_description}\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d')}\n\n")
            
            qa_count = 0
            
            # Process each document
            for document in self.documents:
                title = document.get("title", "Untitled Document")
                f.write(f"## {title}\n\n")
                
                # Write QA pairs
                qa_pairs = document.get("qa_pairs", [])
                if qa_pairs:
                    for i, qa in enumerate(qa_pairs):
                        question = qa.get("question", "")
                        answer = qa.get("answer", "")
                        f.write(f"### Q{i+1}: {question}\n\n{answer}\n\n")
                        qa_count += 1
                else:
                    f.write("No Q&A pairs available for this document.\n\n")
            
            logger.info(f"Generated {qa_filepath} with {qa_count} Q&A pairs")
        
        # Also generate JSON format
        json_filepath = os.path.join(source_dir, "question_answer_pairs.json")
        
        with open(json_filepath, "w", encoding="utf-8") as f:
            qa_data = {
                "source": self.source_description,
                "generated_date": datetime.now().strftime("%Y-%m-%d"),
                "documents": []
            }
            
            for document in self.documents:
                doc_data = {
                    "title": document.get("title", "Untitled Document"),
                    "qa_pairs": document.get("qa_pairs", [])
                }
                qa_data["documents"].append(doc_data)
            
            json.dump(qa_data, f, indent=2)
        
        logger.info(f"Generated {json_filepath}")
    
    def _generate_combined_structure(self):
        """Generate a combined documentation file."""
        # Create a subdirectory for this source
        source_dir = self._create_source_directory()
        
        # Generate a combined markdown file
        combined_filename = "combined_documentation.md"
        combined_filepath = os.path.join(source_dir, combined_filename)
        
        with open(combined_filepath, "w", encoding="utf-8") as f:
            f.write(f"# Combined Documentation: {self.source_description}\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write("## Table of Contents\n\n")
            
            # Generate TOC
            for i, document in enumerate(self.documents):
                title = document.get("title", f"Document {i+1}")
                f.write(f"- [{title}](#{self._anchor(title)})\n")
            
            f.write("\n---\n\n")
            
            # Write each document
            for document in self.documents:
                f.write(self._generate_markdown_document(document))
                f.write("\n\n---\n\n")
            
            logger.info(f"Generated combined documentation: {combined_filepath}")
    
    def _generate_markdown_document(self, document):
        """
        Generate markdown content for a document.
        
        Args:
            document (dict): Document data
            
        Returns:
            str: Markdown content
        """
        title = document.get("title", "Untitled Document")
        improved_summary = document.get("improved_summary", document.get("summary", ""))
        
        # Start with title and metadata
        content = [f"# {title}"]
        
        # Add source information
        if document.get("type") == "markdown":
            content.append(f"Source: {document.get('path', 'Unknown')}")
        elif document.get("type") == "webpage":
            content.append(f"Source: [{document.get('url', 'Unknown')}]({document.get('url', '#')})")
        
        content.append(f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
        content.append("")
        
        # Add summary section
        content.append("## Summary")
        content.append(improved_summary)
        content.append("")
        
        # Add keywords if available
        if document.get("keywords"):
            content.append("## Keywords")
            keywords = document.get("keywords", [])[:20]  # Limit to top 20
            content.append(", ".join(keywords))
            content.append("")
        
        # Add main content sections
        content.append("## Content")
        
        for section in document.get("transformed_sections", []):
            heading = section.get("heading", "")
            level = section.get("level", 2)
            transformed_content = section.get("transformed_content", "")
            
            # Add heading with appropriate level (markdown supports up to 6 levels)
            header_level = min(level + 1, 6)  # Ensure heading level doesn't exceed 6
            content.append(f"{'#' * header_level} {heading}")
            content.append(transformed_content)
            content.append("")
        
        # Add Q&A section if available
        qa_pairs = document.get("qa_pairs", [])
        if qa_pairs:
            content.append("## Questions & Answers")
            
            for i, qa in enumerate(qa_pairs):
                question = qa.get("question", "")
                answer = qa.get("answer", "")
                content.append(f"### Q{i+1}: {question}")
                content.append(answer)
                content.append("")
        
        return "\n".join(content)
    
    def _create_source_directory(self):
        """
        Create a subdirectory for the current source.
        
        Returns:
            str: Path to the source directory
        """
        # Create a safe directory name
        source_name = self._safe_filename(self.source_description)
        if not source_name:
            source_name = "unnamed_source"
        
        source_dir = os.path.join(self.directory, source_name)
        os.makedirs(source_dir, exist_ok=True)
        
        return source_dir
    
    def _generate_metadata(self):
        """Generate a metadata file with information about the generation process."""
        metadata = {
            "source": self.transformed_data.get("source", ""),
            "description": self.source_description,
            "generation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "document_count": len(self.documents),
            "format": self.format,
            "structure": self.structure
        }
        
        # Create a safe directory name
        source_name = self._safe_filename(self.source_description)
        if not source_name:
            source_name = "unnamed_source"
        
        source_dir = os.path.join(self.directory, source_name)
        
        # Write metadata file
        metadata_path = os.path.join(source_dir, "metadata.json")
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)
        
        logger.info(f"Generated metadata file: {metadata_path}")
    
    def _safe_filename(self, filename):
        """
        Convert a string to a safe filename.
        
        Args:
            filename (str): The original filename
            
        Returns:
            str: A safe filename
        """
        # Replace spaces with underscores
        filename = filename.replace(" ", "_")
        
        # Remove or replace special characters
        filename = re.sub(r"[^a-zA-Z0-9_.-]", "", filename)
        
        # Ensure filename isn't too long
        if len(filename) > 50:
            filename = filename[:50]
        
        return filename.lower()
    
    def _anchor(self, text):
        """
        Convert a text to a markdown anchor.
        
        Args:
            text (str): The text
            
        Returns:
            str: A markdown anchor
        """
        # Convert to lowercase
        anchor = text.lower()
        
        # Replace spaces with hyphens
        anchor = anchor.replace(" ", "-")
        
        # Remove special characters
        anchor = re.sub(r"[^a-z0-9-]", "", anchor)
        
        return anchor 