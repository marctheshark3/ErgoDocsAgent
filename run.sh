#!/bin/bash

# ErgoDocsAgent startup script

# Load environment variables
if [ -f .env ]; then
  echo "Loading environment variables from .env"
  export $(grep -v '^#' .env | xargs)
else
  echo "Warning: .env file not found."
  echo "Make sure you have set the OPENAI_API_KEY environment variable."
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

# Check for OpenAI API key
if [ -z "$OPENAI_API_KEY" ]; then
  echo "Warning: OPENAI_API_KEY is not set. Transformation will be skipped."
fi

# Run with provided arguments
echo "Starting ErgoDocsAgent..."
python3 src/main.py "$@" 