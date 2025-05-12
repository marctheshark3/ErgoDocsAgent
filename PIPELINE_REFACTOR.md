# ErgoDocsAgent Pipeline Refactoring

This document outlines the refactoring of the ErgoDocsAgent document processing pipeline to fix JSON parsing issues and implement a more robust architecture.

## Overview of Changes

We've implemented a complete pipeline refactoring with the following improvements:

1. **Improved Source Management**
   - Git repository handling with proper cloning/pulling
   - Document fingerprinting to skip unchanged files
   - Change detection based on commit history
   - Force processing to reprocess all documents when needed

2. **Robust JSON Handling**
   - Created `json_handler.py` with utilities for JSON extraction, cleaning, and validation
   - Added fallback mechanisms for parsing malformed JSON from API responses
   - Implemented validation for QA pairs

3. **Unified AI Client**
   - Created a consistent interface for both OpenAI and Anthropic
   - Improved prompt templates for better response formatting
   - Added retries with exponential backoff
   - Better error handling and logging

4. **Structured Data Storage**
   - Organized directory structure for each pipeline stage
   - Separate storage for raw, cleaned, and processed data
   - Metadata tracking for document processing state

## Directory Structure

The refactored pipeline creates and uses the following directory structure:

```
data/
├── raw/           # Raw content from sources
├── cleaned/       # Cleaned and normalized text
├── summaries/     # Generated summaries
├── qa/            # Question-answer pairs
├── processed/     # Final processed documents
└── metadata/      # Fingerprints and processing metadata
```

## Implementation Guide

Follow these steps to implement the refactored pipeline:

1. **Create Directory Structure**
   
   The new `DocumentPipeline` class will automatically create these directories when initialized.

2. **Install Dependencies**

   No additional dependencies required beyond the existing ones.

3. **New Files**

   We've added the following new files:
   - `src/utils/pipeline.py` - Main pipeline implementation
   - `src/processing/json_handler.py` - JSON processing utilities
   - `src/processing/ai_client.py` - Unified AI client

4. **Modified Files**
   - `src/main.py` - Updated to use the new pipeline

## Usage

Run the pipeline with the following command:

```bash
python run_app.py --now
```

Additional options:
- `--source <url>` - Process only a specific source
- `--force` - Force reprocessing of all documents, ignoring fingerprints
- `--clear-fingerprints` - Clear all document fingerprints without running the pipeline
- `--config <path>` - Specify a custom configuration file

### Force Processing Options

There are two options for forcing document reprocessing:

1. **Full Force Mode (`--force`)**:
   - Completely bypasses document fingerprinting
   - Removes existing Git repositories for a clean clone
   - Treats all files as changed, regardless of actual changes
   - Use this when you want a complete refresh of all data

2. **Clear Fingerprints Only (`--clear-fingerprints`)**:
   - Removes only the document fingerprint files
   - Doesn't remove existing Git repositories
   - Allows the next run to process all documents as if they were new
   - Use this when you want to reprocess documents but don't need to re-clone repositories

Example usage:
```bash
# Run with full force mode
python run_app.py --now --force

# Only clear fingerprints, then run normally
python run_app.py --clear-fingerprints
python run_app.py --now
```

## Fixing JSON Parsing Issues

The main issue we've addressed is the JSON parsing failures seen in the API response logs. The problems were:

1. **Text Preambles**: Responses included text before the JSON data
   - Fixed by extracting only the JSON portion of responses
   - Better prompt engineering to request JSON-only responses

2. **Newlines in JSON Strings**: Caused parsing errors
   - Fixed by properly escaping newlines in JSON strings
   - Added JSON cleaning utilities

3. **Control Characters**: Caused JSON parsing failures
   - Fixed by removing or properly escaping control characters
   - Implemented JSON validation

4. **Malformed JSON Structure**: Some responses weren't valid JSON
   - Fixed with fallback mechanisms for parsing
   - Added multiple parsing attempts with different strategies

## Next Steps

1. Complete the integration with existing extractor and output modules
2. Implement content extraction for different document types (Markdown, HTML, etc.)
3. Add more advanced document change detection
4. Implement advanced content processing (semantic search, vector indexing)

## Testing

To test the new pipeline:

1. Run with a single source first:
   ```bash
   python run_app.py --now --source https://github.com/ergoplatform/ergodocs
   ```

2. Check the logs for any errors:
   ```bash
   tail -f ergo_docs_agent.log
   ```

3. Examine the processed data in the `data/` directory to verify proper processing.

4. If any issues persist, use force processing:
   ```bash
   # Option 1: Full force mode
   python run_app.py --now --force
   
   # Option 2: Clear fingerprints only
   python run_app.py --clear-fingerprints
   python run_app.py --now
   ``` 