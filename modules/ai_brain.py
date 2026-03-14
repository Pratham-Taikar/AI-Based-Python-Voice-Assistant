"""
AI Brain Module
Handles AI-powered conversations using OpenAI API
"""

import os
from openai import OpenAI  # Now pointed at Groq's API
from dotenv import load_dotenv
from config import Config

class AIBrain:
    def __init__(self):
        """
        Initialize AI brain using Groq API via OpenAI-compatible SDK.
        """
        conf = Config()
        api_key = conf.get("api_key", "")
        if not api_key or api_key.strip() == "":
            raise Exception("AI API key not configured")
        # Point client to Groq endpoint
        self.client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
        self.system_prompt = """You are a helpful desktop voice assistant named Jarvis.
        Provide concise, clear, and friendly responses.
        Keep answers under 50 words unless asked for details.
        You help with tasks, answer questions, and provide guidance."""
        self.conversation_history = []
        self.max_history = 10
    
    def think(self, user_input):
        """Get AI response"""
        try:
            # Add user message
            self.conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Keep only recent history
            if len(self.conversation_history) > self.max_history:
                self.conversation_history = self.conversation_history[-self.max_history:]
            
            # Get response
            response = self.client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    *self.conversation_history
                ],
                max_tokens=100,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": ai_response
            })
            
            return ai_response
            
        except Exception as e:
            return f"I'm having trouble thinking right now: {str(e)}"
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []

