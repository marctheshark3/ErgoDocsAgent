"""
Document Processing Pipeline

This module implements the main document processing pipeline with better error handling,
source management, and document fingerprinting to avoid reprocessing unchanged files.
"""

import os
import json
import hashlib
import logging
import subprocess
import datetime
from pathlib import Path
import re

# Setup logging
logger = logging.getLogger(__name__)

class DocumentPipeline:
    """
    Pipeline for processing documentation from various sources.
    The pipeline consists of 4 stages:
    1. Source Management (git clone/pull)
    2. Document Preprocessing (extraction, cleaning, fingerprinting)
    3. Content Processing (AI-powered transformation)
    4. Storage and Output (structured data storage)
    """
    
    def __init__(self, config, console=None):
        """
        Initialize the pipeline with configuration.
        
        Args:
            config (dict): Pipeline configuration
            console: Rich console for output
        """
        self.config = config
        self.console = console
        self.force_processing = config.get('force', False)
        
        if self.force_processing and self.console:
            self.console.print("[bold yellow]Force processing enabled - Will reprocess all documents[/]")
            logger.info("Force processing enabled - Will reprocess all documents")
        
        # Create necessary directories
        self.setup_directories()
    
    def setup_directories(self):
        """Create the directory structure for the pipeline."""
        # Base data directory
        os.makedirs("data", exist_ok=True)
        
        # Pipeline stage directories
        os.makedirs("data/raw", exist_ok=True)        # Raw input data
        os.makedirs("data/cleaned", exist_ok=True)    # Cleaned text
        os.makedirs("data/summaries", exist_ok=True)  # Generated summaries
        os.makedirs("data/qa", exist_ok=True)         # Q&A pairs
        os.makedirs("data/processed", exist_ok=True)  # Final processed data
        
        # Metadata directory for fingerprints and state
        os.makedirs("data/metadata", exist_ok=True)
    
    def run(self, source_override=None):
        """
        Run the complete pipeline.
        
        Args:
            source_override (str): Optional URL to process only a specific source
            
        Returns:
            dict: Pipeline statistics
        """
        sources = self.config['sources']
        if source_override:
            sources = [s for s in sources if s['url'] == source_override]
            if not sources:
                logger.error(f"Source {source_override} not found in configuration")
                return {"error": f"Source {source_override} not found"}
        
        # Track pipeline statistics
        pipeline_stats = {
            "sources": [],
            "total_documents": 0,
            "new_documents": 0,
            "updated_documents": 0,
            "unchanged_documents": 0,
            "errors": 0
        }
        
        # Process each source
        for source in sources:
            source_stats = self._process_source(source)
            pipeline_stats["sources"].append(source_stats)
            pipeline_stats["total_documents"] += source_stats.get("total_documents", 0)
            pipeline_stats["new_documents"] += source_stats.get("new_documents", 0)
            pipeline_stats["updated_documents"] += source_stats.get("updated_documents", 0)
            pipeline_stats["unchanged_documents"] += source_stats.get("unchanged_documents", 0)
            pipeline_stats["errors"] += source_stats.get("errors", 0)
        
        return pipeline_stats
    
    def _process_source(self, source):
        """
        Process a single source through the pipeline.
        
        Args:
            source (dict): Source configuration
            
        Returns:
            dict: Statistics for this source
        """
        source_name = source.get('description', source.get('url', 'Unknown source'))
        logger.info(f"Processing source: {source_name}")
        
        source_stats = {
            "name": source_name,
            "type": source.get("type", "unknown"),
            "total_documents": 0,
            "new_documents": 0,
            "updated_documents": 0,
            "unchanged_documents": 0,
            "errors": 0,
            "status": "FAILED"  # Assume failure until complete
        }
        
        try:
            # Step 1: Source Management
            content = self._manage_source(source)
            
            # Step 2: Document Preprocessing
            documents, doc_stats = self._preprocess_documents(content, source)
            source_stats.update(doc_stats)
            
            # Step 3: Content Processing (if there are documents to process)
            if documents:
                processed_docs, processing_stats = self._process_content(documents, source)
                source_stats.update(processing_stats)
            else:
                processed_docs = []
            
            # Step 4: Storage & Output
            if processed_docs:
                storage_stats = self._store_output(processed_docs, source)
                source_stats.update(storage_stats)
            
            source_stats["status"] = "COMPLETE"
            
        except Exception as e:
            logger.exception(f"Error processing source {source_name}: {str(e)}")
            source_stats["errors"] += 1
        
        return source_stats
    
    def _manage_source(self, source):
        """
        Handle source management (repository cloning, website fetching, etc.)
        
        Args:
            source (dict): Source configuration
            
        Returns:
            object: Fetched content to be processed
        """
        source_type = source.get("type", "")
        url = source.get("url", "")
        
        if source_type == "github":
            return self._manage_git_repository(url, source)
        elif source_type == "website":
            return self._fetch_website_content(url, source)
        else:
            raise ValueError(f"Unsupported source type: {source_type}")
    
    def _manage_git_repository(self, repo_url, source):
        """
        Clone or update a Git repository.
        
        Args:
            repo_url (str): Repository URL
            source (dict): Source configuration
            
        Returns:
            str: Local path to the repository
        """
        # Extract repository name from URL
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        local_path = os.path.join("data/raw", repo_name)
        
        # Handle force flag for Git operations
        if self.force_processing and os.path.exists(local_path):
            # With force flag, remove the existing repo for clean clone
            if self.console:
                self.console.print(f"[bold yellow]Force processing: Removing existing repository at {local_path}[/]")
            logger.info(f"Force processing: Removing existing repository at {local_path}")
            
            # Use subprocess to remove the directory with git metadata
            subprocess.run(["rm", "-rf", local_path], check=True)
        
        if os.path.exists(os.path.join(local_path, ".git")):
            # Repository exists, update it
            logger.info(f"Updating repository: {repo_url}")
            subprocess.run(["git", "pull"], cwd=local_path, check=True)
        else:
            # Clone the repository
            logger.info(f"Cloning repository: {repo_url}")
            subprocess.run(["git", "clone", repo_url, local_path], check=True)
        
        # Record the current commit hash
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=local_path, capture_output=True, text=True, check=True
        )
        current_commit = result.stdout.strip()
        
        # Load previous commit hash if available
        commit_file = os.path.join("data/metadata", f"{repo_name}_commit.txt")
        if os.path.exists(commit_file):
            with open(commit_file, "r") as f:
                previous_commit = f.read().strip()
        else:
            previous_commit = ""
        
        # Get changed files since last commit
        changed_files = []
        if previous_commit and not self.force_processing:
            result = subprocess.run(
                ["git", "diff", "--name-only", previous_commit, current_commit],
                cwd=local_path, capture_output=True, text=True, check=True
            )
            changed_files = result.stdout.splitlines()
        elif self.force_processing:
            # When force processing, treat all files as changed
            result = subprocess.run(
                ["git", "ls-files"],
                cwd=local_path, capture_output=True, text=True, check=True
            )
            changed_files = result.stdout.splitlines()
            if self.console:
                self.console.print(f"[bold yellow]Force processing: Treating all {len(changed_files)} files as changed[/]")
            logger.info(f"Force processing: Treating all {len(changed_files)} files as changed")
        
        # Save current commit
        with open(commit_file, "w") as f:
            f.write(current_commit)
        
        return {
            "local_path": local_path,
            "changed_files": changed_files,
            "current_commit": current_commit,
            "previous_commit": previous_commit
        }
    
    def _fetch_website_content(self, url, source):
        """
        Fetch content from a website.
        
        Args:
            url (str): Website URL
            source (dict): Source configuration
            
        Returns:
            dict: Website content
        """
        # This would use WebsiteIngestion
        # For now, return a placeholder
        return {"url": url, "content": "Website content would be fetched here"}
    
    def _preprocess_documents(self, content, source):
        """
        Preprocess documents from the source content.
        
        Args:
            content: Source content
            source (dict): Source configuration
            
        Returns:
            tuple: (List of preprocessed documents, Document statistics)
        """
        documents = []
        stats = {
            "total_documents": 0,
            "new_documents": 0,
            "updated_documents": 0,
            "unchanged_documents": 0
        }
        
        if source.get("type") == "github" and isinstance(content, dict):
            local_path = content.get("local_path", "")
            changed_files = content.get("changed_files", [])
            
            if self.console:
                self.console.print(f"[bold blue]Preprocessing documents from repository: {len(changed_files)} files to process[/]")
            logger.info(f"Preprocessing documents from repository: {len(changed_files)} files to process")
            
            # Process only markdown files
            markdown_files = [f for f in changed_files if f.endswith(('.md', '.mdx', '.markdown'))]
            
            if self.console:
                self.console.print(f"[bold blue]Found {len(markdown_files)} markdown files to process[/]")
            logger.info(f"Found {len(markdown_files)} markdown files to process")
            
            # Process each markdown file
            for file_path in markdown_files:
                try:
                    full_path = os.path.join(local_path, file_path)
                    if not os.path.exists(full_path):
                        continue
                    
                    # Create a document ID from the file path
                    doc_id = file_path.replace('/', '_').replace('.', '_')
                    
                    # Read the file content
                    with open(full_path, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                    
                    # Extract title from the first heading or use the file name
                    title = os.path.basename(file_path)
                    heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                    if heading_match:
                        title = heading_match.group(1).strip()
                    
                    # Check if the document has changed
                    if self._is_document_changed(doc_id, content):
                        # Split content into sections
                        sections = self._extract_sections(content)
                        
                        # Create the document
                        document = {
                            "id": doc_id,
                            "title": title,
                            "file_path": file_path,
                            "sections": sections,
                            "content": content[:1000] + "..." if len(content) > 1000 else content,  # Truncated for logging
                            "source": source.get("url", ""),
                            "last_updated": datetime.datetime.now().isoformat()
                        }
                        
                        documents.append(document)
                        
                        # Store the cleaned text
                        cleaned_path = os.path.join("data/cleaned", doc_id + ".txt")
                        os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
                        with open(cleaned_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        
                        # Update statistics
                        stats["total_documents"] += 1
                        
                        # Check if this is a new or updated document
                        if os.path.exists(os.path.join("data/metadata", f"{doc_id}_fingerprint.txt")):
                            stats["updated_documents"] += 1
                            if self.console:
                                self.console.print(f"[dim]Updated document: {title[:40]}...[/]")
                        else:
                            stats["new_documents"] += 1
                            if self.console:
                                self.console.print(f"[dim]New document: {title[:40]}...[/]")
                    else:
                        stats["unchanged_documents"] += 1
                        if self.console:
                            self.console.print(f"[dim]Unchanged document: {title[:40]}...[/]")
                
                except Exception as e:
                    logger.error(f"Error processing file {file_path}: {str(e)}")
                    stats["errors"] = stats.get("errors", 0) + 1
            
            if self.console:
                self.console.print(f"[bold green]✓[/] Preprocessed {stats['total_documents']} documents")
            logger.info(f"Preprocessed {stats['total_documents']} documents")
        
        return documents, stats
    
    def _extract_sections(self, content):
        """
        Extract sections from markdown content.
        
        Args:
            content (str): Markdown content
            
        Returns:
            list: List of sections
        """
        sections = []
        current_heading = "Introduction"
        current_level = 0
        current_content = []
        
        # Add a newline to ensure the last section is processed
        content += "\n"
        
        # Process each line
        for line in content.splitlines():
            # Check if it's a heading
            heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if heading_match:
                # If we have content for the current section, save it
                if current_content:
                    sections.append({
                        "heading": current_heading,
                        "level": current_level,
                        "content": "\n".join(current_content).strip()
                    })
                    current_content = []
                
                # Start a new section
                current_level = len(heading_match.group(1))
                current_heading = heading_match.group(2).strip()
            else:
                # Add the line to the current section
                current_content.append(line)
        
        # Add the last section
        if current_content:
            sections.append({
                "heading": current_heading,
                "level": current_level,
                "content": "\n".join(current_content).strip()
            })
        
        return sections
    
    def _process_content(self, documents, source):
        """
        Process documents with AI transformations.
        
        Args:
            documents (list): Preprocessed documents
            source (dict): Source configuration
            
        Returns:
            tuple: (List of processed documents, Processing statistics)
        """
        from src.processing.ai_client import AIClient
        
        processed_docs = []
        stats = {
            "processed_documents": 0,
            "processing_errors": 0,
            "ai_summaries_generated": 0,
            "ai_qa_pairs_generated": 0,
            "fallback_generation_used": 0
        }
        
        if documents:
            if self.console:
                self.console.print(f"[bold blue]Processing {len(documents)} documents with AI[/]")
            logger.info(f"Processing {len(documents)} documents with AI")
            
            # Initialize AI client
            ai_config = self.config.get('ai', {})
            provider_type = ai_config.get('default_provider', 'anthropic')
            model = ai_config.get(f"{provider_type}", {}).get('model')
            
            if self.console:
                self.console.print(f"[bold magenta]Using AI provider:[/] [bold]{provider_type.upper()}[/] | [bold magenta]Model:[/] [bold]{model or 'default'}[/]")
            
            try:
                client = AIClient(
                    provider_type=provider_type,
                    model=model,
                    temperature=ai_config.get(f"{provider_type}", {}).get('temperature', 0.7),
                    max_tokens=ai_config.get(f"{provider_type}", {}).get('max_tokens', 1000)
                )
                
                if not client.is_ready():
                    raise ValueError(f"AI client ({provider_type}) is not properly initialized. Check API keys.")
                
            except Exception as e:
                logger.error(f"Error initializing AI client: {str(e)}")
                if self.console:
                    self.console.print(f"[bold red]Error initializing AI client: {str(e)}[/]")
                    self.console.print("[bold yellow]Falling back to basic document processing without AI[/]")
                # Set client to None to use fallback processing
                client = None
                stats["fallback_generation_used"] = len(documents)
            
            # Process each document
            for idx, document in enumerate(documents):
                try:
                    # Extract basic information
                    doc_id = document.get("id", "unknown")
                    title = document.get("title", "Untitled")
                    
                    if idx % 10 == 0 or idx == len(documents) - 1:
                        if self.console:
                            self.console.print(f"[dim]Processing document {idx+1}/{len(documents)}: {title[:40]}...[/]")
                    
                    # Generate AI content or use fallback
                    if client and client.is_ready():
                        try:
                            # Generate summary with AI
                            summary = client.generate_summary(document)
                            if summary:
                                stats["ai_summaries_generated"] += 1
                            else:
                                # Fallback for summary
                                content = document.get("content", "")
                                summary = content[:200] + "..." if len(content) > 200 else content
                                logger.warning(f"Using fallback summary for document {doc_id}")
                                
                            # Generate Q&A pairs with AI
                            qa_pairs = client.generate_qa_pairs(document)
                            if qa_pairs:
                                stats["ai_qa_pairs_generated"] += 1
                            else:
                                # Fallback for Q&A pairs
                                qa_pairs = self._generate_fallback_qa_pairs(document)
                                logger.warning(f"Using fallback Q&A pairs for document {doc_id}")
                                
                        except Exception as e:
                            logger.error(f"AI processing error for document {doc_id}: {str(e)}")
                            # Use fallback content
                            content = document.get("content", "")
                            summary = content[:200] + "..." if len(content) > 200 else content
                            qa_pairs = self._generate_fallback_qa_pairs(document)
                            stats["fallback_generation_used"] += 1
                    else:
                        # Use fallback content generation
                        content = document.get("content", "")
                        summary = content[:200] + "..." if len(content) > 200 else content
                        qa_pairs = self._generate_fallback_qa_pairs(document)
                        stats["fallback_generation_used"] += 1
                    
                    # Create processed document
                    processed_doc = {
                        "id": doc_id,
                        "title": title,
                        "summary": summary,
                        "qa_pairs": qa_pairs,
                        "sections": document.get("sections", []),
                        "source": document.get("source", ""),
                        "file_path": document.get("file_path", ""),
                        "processed_at": datetime.datetime.now().isoformat(),
                        "ai_processed": client is not None and client.is_ready()
                    }
                    
                    processed_docs.append(processed_doc)
                    stats["processed_documents"] += 1
                    
                except Exception as e:
                    logger.error(f"Error processing document {title}: {str(e)}")
                    stats["processing_errors"] += 1
            
            # Output processing summary
            if self.console:
                self.console.print(f"[bold green]✓[/] Processed {stats['processed_documents']} documents")
                self.console.print(f"[dim]  - AI Summaries: {stats['ai_summaries_generated']}/{len(documents)}[/]")
                self.console.print(f"[dim]  - AI Q&A Pairs: {stats['ai_qa_pairs_generated']}/{len(documents)}[/]")
                if stats["fallback_generation_used"] > 0:
                    self.console.print(f"[dim]  - Fallback generation used: {stats['fallback_generation_used']}/{len(documents)}[/]")
                if stats["processing_errors"] > 0:
                    self.console.print(f"[bold red]  - Errors: {stats['processing_errors']}[/]")
            
            logger.info(f"Processed {stats['processed_documents']} documents: " +
                      f"AI Summaries: {stats['ai_summaries_generated']}, " +
                      f"AI Q&A Pairs: {stats['ai_qa_pairs_generated']}, " +
                      f"Fallbacks: {stats['fallback_generation_used']}, " +
                      f"Errors: {stats['processing_errors']}")
        
        return processed_docs, stats
    
    def _generate_fallback_qa_pairs(self, document):
        """
        Generate fallback Q&A pairs without using AI.
        
        Args:
            document (dict): Document data
            
        Returns:
            list: List of Q&A pairs
        """
        title = document.get("title", "Untitled")
        content = document.get("content", "")
        
        # Create some basic Q&A pairs
        qa_pairs = [
            {"question": "What is this document about?", "answer": content[:200] + "..." if len(content) > 200 else content},
            {"question": "What is the title of this document?", "answer": title}
        ]
        
        # Add more Q&A pairs from sections
        sections = document.get("sections", [])
        for i, section in enumerate(sections[:3]):  # Limit to first 3 sections
            section_heading = section.get("heading", "")
            section_content = section.get("content", "")
            if section_heading and section_content:
                qa_pairs.append({
                    "question": f"What is the '{section_heading}' section about?",
                    "answer": section_content[:100] + "..." if len(section_content) > 100 else section_content
                })
        
        return qa_pairs
    
    def _store_output(self, processed_docs, source):
        """
        Store processed documents in the appropriate format.
        
        Args:
            processed_docs (list): Processed documents
            source (dict): Source configuration
            
        Returns:
            dict: Storage statistics
        """
        stats = {
            "stored_documents": 0,
            "storage_errors": 0
        }
        
        if processed_docs:
            if self.console:
                self.console.print(f"[bold blue]Storing {len(processed_docs)} processed documents[/]")
            logger.info(f"Storing {len(processed_docs)} processed documents")
            
            for doc in processed_docs:
                try:
                    # Extract document information
                    doc_id = doc.get("id", "unknown")
                    title = doc.get("title", "Untitled")
                    
                    # Store summary
                    summary = doc.get("summary", "")
                    summary_path = os.path.join("data/summaries", f"{doc_id}.txt")
                    os.makedirs(os.path.dirname(summary_path), exist_ok=True)
                    with open(summary_path, 'w', encoding='utf-8') as f:
                        f.write(summary)
                    
                    # Store Q&A pairs
                    qa_pairs = doc.get("qa_pairs", [])
                    qa_path = os.path.join("data/qa", f"{doc_id}.json")
                    os.makedirs(os.path.dirname(qa_path), exist_ok=True)
                    with open(qa_path, 'w', encoding='utf-8') as f:
                        json.dump(qa_pairs, f, indent=2)
                    
                    # Store processed document
                    processed_path = os.path.join("data/processed", f"{doc_id}.json")
                    os.makedirs(os.path.dirname(processed_path), exist_ok=True)
                    with open(processed_path, 'w', encoding='utf-8') as f:
                        json.dump(doc, f, indent=2)
                    
                    stats["stored_documents"] += 1
                    
                    if self.console:
                        self.console.print(f"[dim]Stored document: {title[:40]}...[/]")
                
                except Exception as e:
                    logger.error(f"Error storing document {doc_id}: {str(e)}")
                    stats["storage_errors"] += 1
            
            # Store collection index if needed
            try:
                index = {
                    "documents": [
                        {
                            "id": doc.get("id", ""),
                            "title": doc.get("title", ""),
                            "path": f"processed/{doc.get('id', '')}.json"
                        }
                        for doc in processed_docs
                    ],
                    "source": source.get("url", ""),
                    "description": source.get("description", ""),
                    "generated_at": datetime.datetime.now().isoformat(),
                    "document_count": len(processed_docs)
                }
                
                index_path = os.path.join("data/processed", "index.json")
                with open(index_path, 'w', encoding='utf-8') as f:
                    json.dump(index, f, indent=2)
                
                if self.console:
                    self.console.print(f"[bold green]✓[/] Generated document index with {len(processed_docs)} entries")
            except Exception as e:
                logger.error(f"Error generating document index: {str(e)}")
                stats["storage_errors"] += 1
            
            if self.console:
                self.console.print(f"[bold green]✓[/] Stored {stats['stored_documents']} documents")
            logger.info(f"Stored {stats['stored_documents']} documents")
        
        return stats
    
    def _generate_document_fingerprint(self, content):
        """
        Generate a fingerprint for a document to detect changes.
        
        Args:
            content (str): Document content
            
        Returns:
            str: Document fingerprint (MD5 hash)
        """
        if isinstance(content, str):
            return hashlib.md5(content.encode('utf-8')).hexdigest()
        else:
            # If not a string, convert to JSON and hash
            return hashlib.md5(json.dumps(content, sort_keys=True).encode('utf-8')).hexdigest()
    
    def _is_document_changed(self, doc_id, content):
        """
        Check if a document has changed since last processing.
        
        Args:
            doc_id (str): Document identifier
            content: Document content
            
        Returns:
            bool: True if document has changed or is new
        """
        # If force processing is enabled, always treat documents as changed
        if self.force_processing:
            if os.path.exists(os.path.join("data/metadata", f"{doc_id}_fingerprint.txt")):
                logger.debug(f"Force processing: Treating document {doc_id} as changed")
                return True
        
        fingerprint = self._generate_document_fingerprint(content)
        fingerprint_file = os.path.join("data/metadata", f"{doc_id}_fingerprint.txt")
        
        if os.path.exists(fingerprint_file):
            with open(fingerprint_file, "r") as f:
                old_fingerprint = f.read().strip()
            
            if old_fingerprint == fingerprint and not self.force_processing:
                return False  # Document hasn't changed
        
        # Update fingerprint file
        with open(fingerprint_file, "w") as f:
            f.write(fingerprint)
        
        return True  # Document is new or has changed
        
    def clear_fingerprints(self):
        """
        Clear all document fingerprints to force reprocessing.
        This is an alternative to using the force flag, allowing
        selective clearing of fingerprints.
        
        Returns:
            int: Number of fingerprint files removed
        """
        fingerprint_path = os.path.join("data/metadata")
        count = 0
        
        if os.path.exists(fingerprint_path):
            for filename in os.listdir(fingerprint_path):
                if filename.endswith("_fingerprint.txt"):
                    file_path = os.path.join(fingerprint_path, filename)
                    os.remove(file_path)
                    count += 1
        
        if self.console and count > 0:
            self.console.print(f"[bold yellow]Cleared {count} document fingerprints[/]")
        
        logger.info(f"Cleared {count} document fingerprints")
        return count 