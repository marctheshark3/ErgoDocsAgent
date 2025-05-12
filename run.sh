#!/bin/bash

# ErgoDocsAgent startup script

# Load environment variables
if [ -f .env ]; then
  echo "Loading environment variables from .env"
  export $(grep -v '^#' .env | xargs)
else
  echo "Warning: .env file not found."
  echo "Make sure you have set the required API keys (OPENAI_API_KEY or ANTHROPIC_API_KEY)."
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
  echo "Error: Python 3 is required but not installed."
  exit 1
fi

# Check for requirements
if [ ! -f requirements.txt ]; then
  echo "Error: requirements.txt not found."
  exit 1
fi

# Check if dependencies are installed
echo "Checking dependencies..."
if ! python3 -m pip freeze | grep -q 'GitPython'; then
  echo "Installing dependencies..."
  python3 -m pip install -r requirements.txt
fi

# Check for spaCy model
if ! python3 -c "import spacy; spacy.load('en_core_web_sm')" &> /dev/null; then
  echo "Installing spaCy model..."
  python3 -m spacy download en_core_web_sm
fi

# Read config.json to determine default AI provider
DEFAULT_PROVIDER="openai"
if [ -f config.json ]; then
  echo "Reading configuration from config.json..."
  if command -v jq &> /dev/null; then
    DEFAULT_PROVIDER=$(jq -r '.ai.default_provider // "openai"' config.json)
  else
    echo "Note: 'jq' not found. Install it for better config file parsing."
    # Fallback to grep-based detection
    if grep -q '"default_provider".*"anthropic"' config.json; then
      DEFAULT_PROVIDER="anthropic"
    fi
  fi
  echo "Default AI provider: $DEFAULT_PROVIDER"
fi

# Check for API keys based on configured provider
if [ "$DEFAULT_PROVIDER" = "anthropic" ]; then
  if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "Warning: ANTHROPIC_API_KEY is not set but required by your configuration."
    echo "Transformation using Anthropic Claude will be disabled."
  else
    echo "Anthropic API key detected."
  fi
else
  if [ -z "$OPENAI_API_KEY" ]; then
    echo "Warning: OPENAI_API_KEY is not set but required by your configuration."
    echo "Transformation using OpenAI will be disabled."
  else
    echo "OpenAI API key detected."
  fi
fi

# Rotate/clean old log files if they're too large
if [ -f "ergo_docs_agent.log" ] && [ $(stat -f%z "ergo_docs_agent.log") -gt 5000000 ]; then
  echo "Rotating main log file (ergo_docs_agent.log)..."
  mv ergo_docs_agent.log ergo_docs_agent.log.old
fi

if [ -f "api_responses.log" ] && [ $(stat -f%z "api_responses.log") -gt 5000000 ]; then
  echo "Rotating API responses log file (api_responses.log)..."
  mv api_responses.log api_responses.log.old
fi

# Run with provided arguments
echo "Starting ErgoDocsAgent..."
echo "Logs will be written to ergo_docs_agent.log and api_responses.log"
python3 src/main.py "$@"

# Provide information about checking logs after completion
echo ""
echo "Process completed. If you encountered errors, check these log files:"
echo "- Main log: ergo_docs_agent.log"
echo "- API responses log: api_responses.log" 