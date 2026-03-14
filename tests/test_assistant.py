"""
Unit Tests for Voice Assistant
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from assistant import VoiceAssistant
import time

class TestAssistant(unittest.TestCase):
    def setUp(self):
        """Setup test assistant"""
        self.assistant = VoiceAssistant()
    
    def test_time_command(self):
        """Test time command"""
        response = self.assistant.process_command("what time is it")
        self.assertIn("time is", response.lower())
    
    def test_date_command(self):
        """Test date command"""
        response = self.assistant.process_command("what's the date")
        self.assertIn("today is", response.lower())
    
    def test_greet_command(self):
        """Test greeting"""
        response = self.assistant.process_command("hello")
        self.assertIn("hello", response.lower())
    
    def test_response_time(self):
        """Test response speed"""
        start = time.time()
        self.assistant.process_command("what time is it")
        duration = time.time() - start
        self.assertLess(duration, 2.0)
    
    def test_unknown_command(self):
        """Test unknown command"""
        response = self.assistant.process_command("xyzabc123random")
        self.assertIsNotNone(response)
    
    def test_exit_command(self):
        """Test exit command"""
        response = self.assistant.process_command("exit")
        self.assertEqual(response, "exit")
    
    def test_help_command(self):
        """Test help command"""
        response = self.assistant.process_command("help")
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()

