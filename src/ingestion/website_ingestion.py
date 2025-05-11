"""
Website Ingestion Module

This module handles fetching and processing documentation from websites.
"""

import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import os

logger = logging.getLogger(__name__)

class WebsiteIngestion:
    """Class to handle ingestion of documentation from websites."""
    
    def __init__(self, source_config):
        """
        Initialize with the source configuration.
        
        Args:
            source_config (dict): Configuration for the website source
        """
        self.url = source_config['url']
        self.max_depth = source_config.get('max_depth', 2)
        self.description = source_config.get('description', '')
        self.visited_urls = set()
        self.documents = []
        self.base_domain = urlparse(self.url).netloc
        
    def fetch(self):
        """
        Fetch documentation from the website.
        
        Returns:
            dict: A dictionary containing all processed documentation content
        """
        logger.info(f"Fetching documentation from website: {self.url}")
        
        try:
            # Start crawling from the base URL
            self._crawl(self.url, 0)
            
            # Return the processed content
            return {
                "source": self.url,
                "description": self.description,
                "documents": self.documents
            }
            
        except Exception as e:
            logger.error(f"Error fetching website documentation: {e}")
            return {"error": str(e)}
    
    def _crawl(self, url, depth):
        """
        Recursively crawl the website to the specified depth.
        
        Args:
            url (str): The URL to crawl
            depth (int): Current crawl depth
        """
        # Check if we've already visited this URL or exceeded max depth
        if url in self.visited_urls or depth > self.max_depth:
            return
        
        # Add to visited URLs
        self.visited_urls.add(url)
        logger.info(f"Crawling: {url} (depth: {depth})")
        
        try:
            # Fetch the page
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            # Pause to be respectful
            time.sleep(1)
            
            # Parse the HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract content
            self._extract_content(url, soup)
            
            # If we haven't reached max depth, follow links
            if depth < self.max_depth:
                links = soup.find_all('a', href=True)
                for link in links:
                    href = link['href']
                    next_url = urljoin(url, href)
                    
                    # Only follow links within the same domain
                    if urlparse(next_url).netloc == self.base_domain:
                        self._crawl(next_url, depth + 1)
                        
        except requests.RequestException as e:
            logger.error(f"Request error for {url}: {e}")
        except Exception as e:
            logger.error(f"Error crawling {url}: {e}")
    
    def _extract_content(self, url, soup):
        """
        Extract relevant content from the page.
        
        Args:
            url (str): The URL of the page
            soup (BeautifulSoup): The parsed HTML
        """
        # Get title
        title_tag = soup.find('title')
        title = title_tag.get_text() if title_tag else os.path.basename(url)
        
        # Get main content (adjust selectors based on the specific website structure)
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')
        
        if not main_content:
            # Fallback to body if no specific content container found
            main_content = soup.body
        
        if main_content:
            # Remove script and style elements
            for script in main_content(["script", "style"]):
                script.decompose()
            
            # Get all headings
            headings = [h.get_text().strip() for h in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
            
            # Get all paragraphs
            paragraphs = [p.get_text().strip() for p in main_content.find_all('p')]
            
            # Get all code blocks
            code_blocks = []
            for code in main_content.find_all('pre'):
                code_text = code.get_text().strip()
                if code_text:
                    code_blocks.append(code_text)
            
            # Combine content with structure preserved
            content = {
                "title": title,
                "url": url,
                "headings": headings,
                "paragraphs": paragraphs,
                "code_blocks": code_blocks,
                "html_content": str(main_content),
                "type": "webpage"
            }
            
            self.documents.append(content)
            logger.debug(f"Extracted content from {url}")
        else:
            logger.warning(f"No main content found for {url}") 