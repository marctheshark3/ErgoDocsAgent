#!/usr/bin/env python3
"""
Script to create or update the .env file with needed API keys
"""

import os
import sys

def create_env_file():
    """Create or update the .env file"""
    env_file = ".env"
    
    # Check if .env file exists
    if os.path.exists(env_file):
        print(f"Found existing {env_file} file.")
        with open(env_file, 'r') as f:
            current_content = f.read()
    else:
        print(f"No {env_file} file found. Creating a new one.")
        current_content = ""
    
    # Check if OPENAI_API_KEY is already in the file
    if "OPENAI_API_KEY" in current_content:
        print("OPENAI_API_KEY already exists in .env file.")
        api_key = input("Enter a new OpenAI API key (leave empty to keep existing): ").strip()
        if api_key:
            lines = current_content.splitlines()
            updated_lines = []
            for line in lines:
                if line.startswith("OPENAI_API_KEY="):
                    updated_lines.append(f"OPENAI_API_KEY={api_key}")
                else:
                    updated_lines.append(line)
            updated_content = "\n".join(updated_lines)
        else:
            print("Keeping existing OpenAI API key.")
            updated_content = current_content
    else:
        # Ask for the API key
        api_key = input("Enter your OpenAI API key: ").strip()
        if not api_key:
            print("Error: OpenAI API key is required.")
            sys.exit(1)
        
        # Prepare updated content
        if current_content and not current_content.endswith("\n"):
            current_content += "\n"
        
        updated_content = current_content + f"OPENAI_API_KEY={api_key}\n"
    
    # Add any other required variables
    variables_to_check = {
        "LOG_LEVEL": "INFO",
        "OUTPUT_DIR": "output",
        "MAX_DOCUMENTS": "100",
        "MAX_DEPTH": "3"
    }
    
    for var, default in variables_to_check.items():
        if var not in current_content:
            add_var = input(f"Add {var}? (default: {default}) [y/N]: ").strip().lower()
            if add_var == 'y':
                custom_value = input(f"Value for {var} (default: {default}): ").strip()
                value = custom_value if custom_value else default
                updated_content += f"{var}={value}\n"
    
    # Write the updated content
    with open(env_file, 'w') as f:
        f.write(updated_content)
    
    print(f"{env_file} file has been updated.")
    print("You can now run the OpenAI test script: python test_openai.py")

if __name__ == "__main__":
    create_env_file() 