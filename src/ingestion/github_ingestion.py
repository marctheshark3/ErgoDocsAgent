"""
GitHub Repository Ingestion Module

This module handles fetching and processing documentation from GitHub repositories.
"""

import os
import tempfile
import logging
import shutil
from git import Repo
from git.exc import GitCommandError
import glob
import markdown
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class GitHubIngestion:
    """Class to handle ingestion of documentation from GitHub repositories."""
    
    def __init__(self, source_config):
        """
        Initialize with the source configuration.
        
        Args:
            source_config (dict): Configuration for the GitHub source
        """
        self.url = source_config['url']
        self.branch = source_config.get('branch', 'main')
        self.description = source_config.get('description', '')
        self.temp_dir = None
        
    def fetch(self):
        """
        Fetch documentation from the GitHub repository.
        
        Returns:
            dict: A dictionary containing all processed documentation content
        """
        logger.info(f"Fetching documentation from GitHub: {self.url}")
        
        # Create a temporary directory
        self.temp_dir = tempfile.mkdtemp()
        logger.info(f"Created temporary directory: {self.temp_dir}")
        
        try:
            # Clone the repository
            logger.info(f"Cloning repository {self.url} branch {self.branch}")
            Repo.clone_from(self.url, self.temp_dir, branch=self.branch, depth=1)
            
            # Process the repository content
            return self._process_repo_content()
            
        except GitCommandError as e:
            logger.error(f"Git error: {e}")
            return {"error": str(e)}
        except Exception as e:
            logger.error(f"Error fetching GitHub documentation: {e}")
            return {"error": str(e)}
        finally:
            # Clean up the temporary directory
            if self.temp_dir and os.path.exists(self.temp_dir):
                shutil.rmtree(self.temp_dir)
                logger.info(f"Removed temporary directory: {self.temp_dir}")
    
    def _process_repo_content(self):
        """
        Process the content of the cloned repository.
        
        Returns:
            dict: A dictionary containing all processed documentation content
        """
        result = {
            "source": self.url,
            "description": self.description,
            "documents": []
        }
        
        # Look for markdown files
        markdown_files = glob.glob(os.path.join(self.temp_dir, "**", "*.md"), recursive=True)
        logger.info(f"Found {len(markdown_files)} markdown files")
        
        # Process each markdown file
        for file_path in markdown_files:
            try:
                relative_path = os.path.relpath(file_path, self.temp_dir)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Parse markdown to extract text and structure
                html_content = markdown.markdown(content)
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # Get title from first heading or filename
                title = soup.find(['h1', 'h2'])
                title = title.get_text() if title else os.path.basename(file_path)
                
                # Store the document information
                document = {
                    "title": title,
                    "path": relative_path,
                    "content": content,
                    "html_content": html_content,
                    "headings": [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])],
                    "type": "markdown"
                }
                
                result["documents"].append(document)
                logger.debug(f"Processed {relative_path}")
                
            except Exception as e:
                logger.error(f"Error processing {file_path}: {e}")
        
        return result 