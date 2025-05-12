# ErgoDocsAgent

ErgoDocsAgent is an AI-powered documentation processing tool designed to automate the extraction, transformation, and generation of LLM-optimized documentation from sources like GitHub repositories and websites, with a focus on Ergo Platform documentation.

## Features

- **Multi-Source Ingestion**: Fetches documentation from GitHub repositories and websites
- **Smart Processing**: Extracts key information using NLP techniques
- **AI-Powered Transformation**: Uses OpenAI to optimize content for LLMs
- **Multiple Output Formats**: Generates Markdown and JSON outputs
- **Periodic Execution**: Supports scheduled runs for keeping documentation updated
- **Flexible Configuration**: Easy to configure for different sources and output formats

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ErgoDocsAgent.git
cd ErgoDocsAgent
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Download the spaCy model:
```bash
python -m spacy download en_core_web_sm
```

4. Create a `.env` file based on the example:
```bash
cp env.example .env
```

5. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Basic Usage

Run the script with default configuration:

```bash
python src/main.py
```

### Command Line Options

- `--config`: Path to configuration file (default: `config.json`)
- `--source`: Process only a specific source URL
- `--schedule`: Run in scheduled mode
- `--now`: Run immediately, then exit

### Examples

Process a specific source:
```bash
python src/main.py --source https://github.com/ergoplatform/ergodocs
```

Run in scheduled mode:
```bash
python src/main.py --schedule
```

### Configuration

Edit `config.json` to customize sources, outputs, and scheduling:

```json
{
  "sources": [
    {
      "type": "github",
      "url": "https://github.com/ergoplatform/ergodocs",
      "branch": "main",
      "description": "Ergo Platform Documentation"
    }
  ],
  "output": {
    "format": "markdown",
    "directory": "output",
    "structure": "topic"
  },
  "schedule": {
    "frequency": "weekly",
    "day_of_week": "monday",
    "time": "00:00"
  }
}
```

## Output Structure

The tool generates the following output:

- `output/<source_name>/`: Directory for each source
  - Individual Markdown files for each document
  - JSON files with structured data
  - `question_answer_pairs.md`: Consolidated Q&A 
  - `combined_documentation.md`: Combined documentation (optional)
  - `metadata.json`: Information about the generation process

## Project Structure

```
ErgoDocsAgent/
├── config.json               # Configuration file
├── requirements.txt          # Python dependencies
├── env.example               # Example environment variables
├── diagrams.md               # Architecture diagrams
├── src/                      # Source code
│   ├── main.py               # Main entry point
│   ├── ingestion/            # Source ingestion modules
│   ├── processing/           # Content processing modules
│   ├── output/               # Output generation modules
│   ├── scheduler/            # Job scheduling
│   └── utils/                # Utility functions
└── output/                   # Generated documentation
```

## Architecture Diagrams

The system architecture and workflows are documented with Mermaid diagrams in [diagrams.md](./diagrams.md), which includes:

- Component Architecture
- Sequence Diagram
- Process Flow
- Class Diagram

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# AI Agent Digital Library

Ergo Docs Agent is an AI-powered documentation system for Ergo Platform, featuring:

- Retrieval of official documentation with context
- Multiple AI models with unique capabilities
- Smart document handling and validation

## New Feature: MCP Servers Integration

The AI Agent Digital Library now integrates with five Model Context Protocol (MCP) servers to enhance document processing capabilities:

1. **GitHub MCP Server**: Access GitHub repositories for ingestion, updates, and research
2. **Filesystem MCP Server**: Manage document storage with read/write file operations
3. **Qdrant MCP Server**: Power RAG capabilities with vector database integration
4. **Brave Search MCP Server**: Discover web resources via Brave Search API
5. **Firecrawl MCP Server**: Scrape and crawl websites for content ingestion

These modular MCP servers support four key pipelines:
- **Ingestion Pipeline**: Process new or updated documents
- **Update Pipeline**: Periodically refresh existing documents
- **Research Pipeline**: Search for new data sources
- **Validation Pipeline**: Assess document quality and relevance

## Getting Started

1. See [mcp_setup.md](mcp_setup.md) for detailed setup instructions for all MCP servers
2. Configure API keys in your `.env` file (copy from `env.example`)
3. Start the servers using Docker Compose:
   ```bash
   docker-compose up -d
   ```

## Architecture

The system uses a modular design where each MCP server is an independent component with standardized JSON-RPC interfaces. This allows servers to be replaced with alternatives if needed without affecting the overall system.

AI agents orchestrate the document processing workflows, using the MCP servers as tools to access external data sources, process documents, and serve content to users via RAG.