#!/usr/bin/env python3
"""
Download required spaCy model for ErgoDocsAgent.
"""

import subprocess
import sys

def download_spacy_model():
    """Download the English spaCy model."""
    print("Downloading spaCy model: en_core_web_sm")
    try:
        # Try to import spacy to check if it's installed
        import spacy
        
        # Download the model
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
        
        # Try to load the model to verify installation
        spacy.load("en_core_web_sm")
        print("spaCy model successfully installed!")
        
    except ImportError:
        print("Error: spaCy is not installed. Please install it first with:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("Error: Failed to download the spaCy model.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_spacy_model() 