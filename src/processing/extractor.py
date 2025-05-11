"""
Content Extractor Module

This module extracts structured information from documentation content.
"""

import logging
import re
import spacy
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class Extractor:
    """Class to extract structured information from documentation content."""
    
    def __init__(self, content_data):
        """
        Initialize with the content data from ingestion.
        
        Args:
            content_data (dict): The data from the ingestion phase
        """
        self.content_data = content_data
        self.documents = content_data.get("documents", [])
        
        # Load spaCy model for NLP processing
        try:
            self.nlp = spacy.load("en_core_web_sm")
            logger.info("Loaded spaCy model: en_core_web_sm")
        except OSError:
            logger.warning("Downloading spaCy model: en_core_web_sm")
            from spacy.cli import download
            download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")
    
    def extract(self):
        """
        Extract structured information from the content.
        
        Returns:
            dict: Extracted structured data
        """
        logger.info(f"Extracting information from {len(self.documents)} documents")
        
        extracted_data = {
            "source": self.content_data.get("source", ""),
            "description": self.content_data.get("description", ""),
            "documents": []
        }
        
        for document in self.documents:
            try:
                # Process based on document type
                if document.get("type") == "markdown":
                    processed_doc = self._process_markdown(document)
                elif document.get("type") == "webpage":
                    processed_doc = self._process_webpage(document)
                else:
                    logger.warning(f"Unknown document type: {document.get('type')}")
                    continue
                
                extracted_data["documents"].append(processed_doc)
                
            except Exception as e:
                logger.error(f"Error extracting data from document: {e}")
        
        return extracted_data
    
    def _process_markdown(self, document):
        """
        Process a markdown document.
        
        Args:
            document (dict): The markdown document data
            
        Returns:
            dict: Processed document with extracted information
        """
        title = document.get("title", "")
        content = document.get("content", "")
        html_content = document.get("html_content", "")
        
        # Extract sections using headings as delimiters
        sections = self._extract_sections(html_content)
        
        # Extract code samples
        code_blocks = self._extract_code_blocks(content)
        
        # Extract entities and keywords using spaCy
        entities, keywords = self._extract_nlp_info(content)
        
        # Create structured document
        processed_doc = {
            "title": title,
            "path": document.get("path", ""),
            "type": "markdown",
            "sections": sections,
            "code_blocks": code_blocks,
            "entities": entities,
            "keywords": keywords,
            "summary": self._generate_summary(content)
        }
        
        return processed_doc
    
    def _process_webpage(self, document):
        """
        Process a webpage document.
        
        Args:
            document (dict): The webpage document data
            
        Returns:
            dict: Processed document with extracted information
        """
        title = document.get("title", "")
        paragraphs = document.get("paragraphs", [])
        html_content = document.get("html_content", "")
        
        # Create combined content for NLP processing
        content = " ".join(paragraphs)
        
        # Extract sections using headings as delimiters
        sections = self._extract_sections(html_content)
        
        # Extract code samples
        code_blocks = document.get("code_blocks", [])
        
        # Extract entities and keywords using spaCy
        entities, keywords = self._extract_nlp_info(content)
        
        # Create structured document
        processed_doc = {
            "title": title,
            "url": document.get("url", ""),
            "type": "webpage",
            "sections": sections,
            "code_blocks": code_blocks,
            "entities": entities,
            "keywords": keywords,
            "summary": self._generate_summary(content)
        }
        
        return processed_doc
    
    def _extract_sections(self, html_content):
        """
        Extract sections from HTML content using headings as delimiters.
        
        Args:
            html_content (str): HTML content
            
        Returns:
            list: List of sections with headings and content
        """
        sections = []
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Find all headings
        headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        
        for i, heading in enumerate(headings):
            # Get heading text and level
            heading_text = heading.get_text().strip()
            heading_level = int(heading.name[1])
            
            # Get content: all elements until the next heading
            content = []
            current = heading.next_sibling
            
            while current and (i == len(headings) - 1 or current != headings[i + 1]):
                if hasattr(current, "name") and current.name not in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                    text = current.get_text().strip()
                    if text:
                        content.append(text)
                current = current.next_sibling
                if not current:
                    break
            
            # Add section if it has content
            if content:
                sections.append({
                    "heading": heading_text,
                    "level": heading_level,
                    "content": "\n".join(content)
                })
        
        return sections
    
    def _extract_code_blocks(self, content):
        """
        Extract code blocks from markdown content.
        
        Args:
            content (str): Markdown content
            
        Returns:
            list: List of code blocks
        """
        # Pattern for code blocks: ```language\ncode\n```
        pattern = r"```(?:(\w+))?\n([\s\S]*?)\n```"
        matches = re.findall(pattern, content)
        
        code_blocks = []
        for language, code in matches:
            code_blocks.append({
                "language": language if language else "text",
                "code": code.strip()
            })
        
        return code_blocks
    
    def _extract_nlp_info(self, content):
        """
        Extract entities and keywords using spaCy.
        
        Args:
            content (str): Text content
            
        Returns:
            tuple: (entities, keywords)
        """
        # Limit content length for processing efficiency
        content = content[:100000]  # Process only first 100k chars
        
        doc = self.nlp(content)
        
        # Extract named entities
        entities = []
        for ent in doc.ents:
            entities.append({
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char
            })
        
        # Extract keywords (nouns and technical terms)
        keywords = []
        seen = set()
        
        for token in doc:
            # Check if token is a noun, proper noun, or part of a compound
            if (token.pos_ in ["NOUN", "PROPN"] or 
                (token.dep_ == "compound" and token.head.pos_ in ["NOUN", "PROPN"])):
                
                # Get the lemmatized form
                lemma = token.lemma_.lower()
                
                # Only add keywords with min length that we haven't seen
                if len(lemma) > 3 and lemma not in seen:
                    keywords.append(lemma)
                    seen.add(lemma)
        
        return entities, keywords
    
    def _generate_summary(self, content):
        """
        Generate a summary of the content.
        
        Args:
            content (str): Text content
            
        Returns:
            str: Generated summary
        """
        # Limit content length
        if len(content) > 100000:
            content = content[:100000]
        
        # Simple extractive summarization using spaCy
        doc = self.nlp(content)
        
        # Get the most important sentences (basic implementation)
        sentences = [sent.text.strip() for sent in doc.sents]
        
        # Take the first 3-5 sentences as a simple summary
        summary_length = min(5, len(sentences))
        summary = " ".join(sentences[:summary_length])
        
        return summary 