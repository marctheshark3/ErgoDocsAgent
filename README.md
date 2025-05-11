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
├── src/                      # Source code
│   ├── main.py               # Main entry point
│   ├── ingestion/            # Source ingestion modules
│   ├── processing/           # Content processing modules
│   ├── output/               # Output generation modules
│   ├── scheduler/            # Job scheduling
│   └── utils/                # Utility functions
└── output/                   # Generated documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.