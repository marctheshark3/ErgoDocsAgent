#!/bin/bash

# Load environment variables from .env if present
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Check for OpenAI API key
if [ -z "$OPENAI_API_KEY" ]; then
  echo "Warning: OPENAI_API_KEY is not set. Transformation will be skipped."
fi

# Run with provided arguments
echo "Starting ErgoDocsAgent..."
exec python /app/run_app.py "$@" 