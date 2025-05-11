"""
Configuration Loader Module

This module handles loading and validating configuration settings.
"""

import os
import json
import logging

logger = logging.getLogger(__name__)

class ConfigLoader:
    """Class to load and validate configuration settings."""
    
    def __init__(self, config_path):
        """
        Initialize with the path to the configuration file.
        
        Args:
            config_path (str): Path to the configuration file
        """
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self):
        """
        Load the configuration from file.
        
        Returns:
            dict: Configuration settings
        """
        try:
            if not os.path.exists(self.config_path):
                logger.error(f"Configuration file not found: {self.config_path}")
                return self._create_default_config()
            
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            
            # Validate the configuration
            valid_config = self._validate_config(config)
            
            return valid_config
            
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in configuration file: {self.config_path}")
            return self._create_default_config()
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            return self._create_default_config()
    
    def _validate_config(self, config):
        """
        Validate the configuration and set defaults for missing values.
        
        Args:
            config (dict): Configuration to validate
            
        Returns:
            dict: Validated configuration
        """
        # Check for required sections
        if "sources" not in config:
            logger.warning("No sources defined in configuration, using default")
            config["sources"] = [self._default_source()]
        
        # Ensure each source has required fields
        for i, source in enumerate(config["sources"]):
            if "type" not in source:
                logger.warning(f"Source {i} missing type, assuming github")
                source["type"] = "github"
            
            if "url" not in source:
                logger.warning(f"Source {i} missing URL, using default")
                source["url"] = "https://github.com/ergoplatform/ergodocs"
        
        # Check for output configuration
        if "output" not in config:
            logger.warning("No output configuration, using default")
            config["output"] = {
                "format": "markdown",
                "directory": "output",
                "structure": "topic"
            }
        else:
            # Set defaults for missing output fields
            output = config["output"]
            if "format" not in output:
                output["format"] = "markdown"
            if "directory" not in output:
                output["directory"] = "output"
            if "structure" not in output:
                output["structure"] = "topic"
        
        # Check for processing configuration
        if "processing" not in config:
            logger.warning("No processing configuration, using default")
            config["processing"] = {
                "summarize": True,
                "extract_code_samples": True,
                "generate_qa_pairs": True
            }
        
        # Check for schedule configuration
        if "schedule" not in config:
            logger.warning("No schedule configuration, using default")
            config["schedule"] = {
                "frequency": "weekly",
                "day_of_week": "monday",
                "time": "00:00"
            }
        
        # Check for OpenAI configuration
        if "openai" not in config:
            logger.warning("No OpenAI configuration, using default")
            config["openai"] = {
                "model": "gpt-4"
            }
        
        return config
    
    def _create_default_config(self):
        """
        Create a default configuration.
        
        Returns:
            dict: Default configuration
        """
        default_config = {
            "sources": [self._default_source()],
            "output": {
                "format": "markdown",
                "directory": "output",
                "structure": "topic"
            },
            "processing": {
                "summarize": True,
                "extract_code_samples": True,
                "generate_qa_pairs": True
            },
            "schedule": {
                "frequency": "weekly",
                "day_of_week": "monday",
                "time": "00:00"
            },
            "openai": {
                "model": "gpt-4"
            }
        }
        
        # Write the default configuration to file
        try:
            with open(self.config_path, 'w') as f:
                json.dump(default_config, f, indent=2)
            logger.info(f"Created default configuration file: {self.config_path}")
        except Exception as e:
            logger.error(f"Error writing default configuration: {e}")
        
        return default_config
    
    def _default_source(self):
        """
        Create a default source configuration.
        
        Returns:
            dict: Default source configuration
        """
        return {
            "type": "github",
            "url": "https://github.com/ergoplatform/ergodocs",
            "branch": "main",
            "description": "Ergo Platform Documentation Repository"
        }
    
    def get_config(self):
        """
        Get the configuration.
        
        Returns:
            dict: Configuration settings
        """
        return self.config
    
    def save_config(self, config):
        """
        Save configuration to file.
        
        Args:
            config (dict): Configuration to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=2)
            logger.info(f"Saved configuration to: {self.config_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving configuration: {e}")
            return False 