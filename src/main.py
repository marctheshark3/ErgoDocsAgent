#!/usr/bin/env python3
"""
ErgoDocsAgent - Documentation Processing AI Agent

This script ingests documentation from various sources, processes it,
and generates LLM-optimized documentation files.
"""

import os
import json
import logging
import argparse
from dotenv import load_dotenv

# Import our modules
from src.ingestion.github_ingestion import GitHubIngestion
from src.ingestion.website_ingestion import WebsiteIngestion
from src.processing.extractor import Extractor
from src.processing.transformer import Transformer
from src.output.generator import DocumentationGenerator
from src.scheduler.job_scheduler import JobScheduler
from src.utils.config_loader import ConfigLoader

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ergo_docs_agent.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def load_config(config_path):
    """Load the configuration file."""
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading config file: {e}")
        raise

def run_pipeline(config, source_override=None):
    """Run the complete documentation processing pipeline."""
    logger.info("Starting documentation processing pipeline")
    
    sources = config['sources']
    if source_override:
        sources = [s for s in sources if s['url'] == source_override]
        if not sources:
            logger.error(f"Source {source_override} not found in configuration")
            return
    
    # Process each source
    for source in sources:
        logger.info(f"Processing source: {source['description']}")
        
        # Ingest content based on source type
        if source['type'] == 'github':
            ingestion = GitHubIngestion(source)
            content = ingestion.fetch()
        elif source['type'] == 'website':
            ingestion = WebsiteIngestion(source)
            content = ingestion.fetch()
        else:
            logger.warning(f"Unknown source type: {source['type']}")
            continue
        
        # Extract information from content
        extractor = Extractor(content)
        extracted_data = extractor.extract()
        
        # Transform content for LLM optimization
        transformer = Transformer(extracted_data, config['openai'])
        transformed_data = transformer.transform()
        
        # Generate output files
        generator = DocumentationGenerator(
            transformed_data, 
            config['output'],
            source['description']
        )
        generator.generate()
    
    logger.info("Documentation processing pipeline completed")

def main():
    """Main entry point for the script."""
    # Load environment variables
    load_dotenv()
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='ErgoDocsAgent - Documentation Processing AI Agent')
    parser.add_argument('--config', type=str, default='config.json', help='Path to configuration file')
    parser.add_argument('--source', type=str, help='Process only a specific source URL')
    parser.add_argument('--schedule', action='store_true', help='Run in scheduled mode')
    parser.add_argument('--now', action='store_true', help='Run immediately, then exit')
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    # Run modes
    if args.now:
        run_pipeline(config, args.source)
    elif args.schedule:
        scheduler = JobScheduler(config['schedule'])
        scheduler.add_job(run_pipeline, config, args.source)
        scheduler.start()
    else:
        run_pipeline(config, args.source)

if __name__ == "__main__":
    main() 