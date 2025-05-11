#!/usr/bin/env python3
"""
Test script to verify the virtual environment setup
"""

import sys
import importlib

# List of packages to test with correct import names
packages = [
    "spacy",
    "numpy",
    "transformers",
    "openai",
    "git", # GitPython's import name is 'git'
    "bs4", # beautifulsoup4's import name is 'bs4'
    "scrapy",
    "apscheduler",
    "markdown", # Markdown's import name is lowercase
    "reportlab",
    "dotenv", # python-dotenv's import name is 'dotenv'
    "requests",
    "tqdm"
]

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print("\nTesting package imports:")

for package in packages:
    try:
        # Handle packages with hyphens
        package_name = package.replace("-", "_").split('==')[0]
        module = importlib.import_module(package_name)
        print(f"✅ {package}: {module.__version__ if hasattr(module, '__version__') else 'OK'}")
    except ImportError as e:
        print(f"❌ {package}: Failed - {str(e)}")

# Test spaCy model
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    print("\n✅ spaCy model 'en_core_web_sm' loaded successfully")
    
    # Test spaCy with a simple example
    doc = nlp("This is a test sentence for spaCy to analyze.")
    print(f"✅ spaCy processing test: identified {len(doc.ents)} entities and {len(doc)} tokens")
except Exception as e:
    print(f"\n❌ spaCy model test failed: {str(e)}")

print("\nEnvironment test completed.") 