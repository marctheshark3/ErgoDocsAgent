#!/usr/bin/env python3
"""
Test script to verify ErgoDocsAgent installation and dependencies.
"""

import sys
import importlib
import os

def check_dependency(module_name, import_name=None):
    """Check if a dependency is installed."""
    if import_name is None:
        import_name = module_name
    
    try:
        importlib.import_module(import_name)
        print(f"✅ {module_name} is installed")
        return True
    except ImportError:
        print(f"❌ {module_name} is NOT installed")
        return False

def check_spacy_model():
    """Check if the spaCy model is installed."""
    try:
        import spacy
        try:
            spacy.load("en_core_web_sm")
            print("✅ spaCy model 'en_core_web_sm' is installed")
            return True
        except OSError:
            print("❌ spaCy model 'en_core_web_sm' is NOT installed")
            return False
    except ImportError:
        print("❌ spaCy is NOT installed")
        return False

def check_openai_key():
    """Check if the OpenAI API key is set."""
    key = os.environ.get("OPENAI_API_KEY")
    if key:
        masked_key = key[:4] + "..." + key[-4:]
        print(f"✅ OPENAI_API_KEY is set ({masked_key})")
        return True
    else:
        print("❌ OPENAI_API_KEY is NOT set")
        return False

def check_required_files():
    """Check if all required files exist."""
    required_files = [
        "config.json",
        "requirements.txt",
        "src/main.py"
    ]
    
    all_found = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} is missing")
            all_found = False
    
    return all_found

def run_tests():
    """Run all installation tests."""
    print("\n===== TESTING ERGODOCSAGENT INSTALLATION =====\n")
    
    # Check required files
    print("\n----- Required Files -----")
    files_ok = check_required_files()
    
    # Check dependencies
    print("\n----- Dependencies -----")
    deps_ok = True
    deps_ok &= check_dependency("GitPython", "git")
    deps_ok &= check_dependency("beautifulsoup4", "bs4")
    deps_ok &= check_dependency("spacy")
    deps_ok &= check_dependency("transformers")
    deps_ok &= check_dependency("openai")
    deps_ok &= check_dependency("APScheduler", "apscheduler")
    deps_ok &= check_dependency("markdown")
    deps_ok &= check_dependency("python-dotenv", "dotenv")
    
    # Check spaCy model
    print("\n----- spaCy Model -----")
    spacy_ok = check_spacy_model()
    
    # Check OpenAI API key
    print("\n----- OpenAI API Key -----")
    openai_ok = check_openai_key()
    
    # Print summary
    print("\n===== TEST SUMMARY =====")
    print(f"Required Files: {'✅ OK' if files_ok else '❌ MISSING'}")
    print(f"Dependencies: {'✅ OK' if deps_ok else '❌ INCOMPLETE'}")
    print(f"spaCy Model: {'✅ OK' if spacy_ok else '❌ MISSING'}")
    print(f"OpenAI API Key: {'✅ OK' if openai_ok else '❌ MISSING'}")
    
    if files_ok and deps_ok and spacy_ok and openai_ok:
        print("\n🎉 All tests passed! ErgoDocsAgent is ready to use.")
        print("Run './run.sh' to start processing documentation.\n")
        return 0
    else:
        print("\n⚠️ Some tests failed. Please fix the issues before running ErgoDocsAgent.")
        if not deps_ok:
            print("To install dependencies, run: pip install -r requirements.txt")
        if not spacy_ok:
            print("To install the spaCy model, run: python download_spacy_model.py")
        if not openai_ok:
            print("Set the OPENAI_API_KEY environment variable or create a .env file.")
        print("")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests()) 