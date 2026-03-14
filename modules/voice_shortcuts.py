"""
Voice Shortcuts Module
Allows users to create custom command sequences
"""

import json
import os

class VoiceShortcuts:
    def __init__(self):
        self.shortcuts_file = "shortcuts.json"
        self.shortcuts = self.load_shortcuts()
    
    def load_shortcuts(self):
        """Load shortcuts"""
        if os.path.exists(self.shortcuts_file):
            try:
                with open(self.shortcuts_file, 'r') as f:
                    return json.load(f)
            except:
                return self.get_default_shortcuts()
        return self.get_default_shortcuts()
    
    def get_default_shortcuts(self):
        """Default shortcuts"""
        return {
            "study mode": [
                "open notepad",
                "open youtube",
                "focus for 25 minutes on studying"
            ],
            "work mode": [
                "open browser",
                "open calculator"
            ]
        }
    
    def save_shortcuts(self):
        """Save shortcuts"""
        with open(self.shortcuts_file, 'w') as f:
            json.dump(self.shortcuts, f, indent=4)
    
    def add_shortcut(self, name, commands):
        """Add shortcut"""
        self.shortcuts[name.lower()] = commands
        self.save_shortcuts()
        return f"Shortcut '{name}' created"
    
    def get_shortcut(self, name):
        """Get shortcut"""
        return self.shortcuts.get(name.lower())
    
    def list_shortcuts(self):
        """List shortcuts"""
        if self.shortcuts:
            result = "Available shortcuts:\n"
            for name in self.shortcuts.keys():
                result += f"- {name}\n"
            return result
        return "No shortcuts"

