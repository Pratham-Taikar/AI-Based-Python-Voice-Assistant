"""
Configuration Manager
Handles application settings and user preferences
"""

import json
import os

class Config:
    def __init__(self):
        self.config_file = "config.json"
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return self.get_default_config()
    
    def get_default_config(self):
        """Default configuration"""
        return {
            "assistant_name": "Jarvis",
            "user_name": "User",
            "voice_rate": 180,
            "voice_volume": 0.9,
            "ai_enabled": True,
            "wake_word": "hey jarvis",
            "theme": "dark",
            "language": "en-US",
            "api_key": ""
        }
    
    def save_config(self):
        """Save configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def get(self, key, default=None):
        """Get config value"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """Set config value"""
        self.config[key] = value
        self.save_config()

