#!/usr/bin/env python3
"""
Wrapper script for running the ErgoDocsAgent with proper imports
"""

import os
import sys
import subprocess

# Add the current directory to Python path
sys.path.insert(0, os.path.abspath('.'))

# Now we can import from the src package
from src.main import main

if __name__ == "__main__":
    # Pass through any command line arguments
    main() 