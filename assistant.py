"""
AI Desktop Assistant - Main Module
Handles voice recognition, speech synthesis, and command processing
"""

import speech_recognition as sr
import pyttsx3
import datetime
import os
import subprocess
import webbrowser
import platform
from pathlib import Path
import psutil

# Try to import AI brain
try:
    from modules.ai_brain import AIBrain
    AI_AVAILABLE = True
except:
    AI_AVAILABLE = False

class VoiceAssistant:
    def __init__(self):
        """Initialize the voice assistant"""
        print("Initializing AI Assistant...")
        
        # Text-to-Speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)
        self.engine.setProperty('volume', 0.9)
        
        # Speech Recognition
        self.recognizer = sr.Recognizer()
        
        # Assistant name
        self.name = "Jarvis"
        
        # AI Integration
        if AI_AVAILABLE:
            try:
                self.ai_brain = AIBrain()
                self.ai_enabled = True
            except:
                self.ai_enabled = False
        else:
            self.ai_enabled = False
        
        print(f"✓ {self.name} initialized successfully!")
        if self.ai_enabled:
            print("✓ AI Brain activated!")
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"{self.name}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen to user's voice command"""
        try:
            with sr.Microphone() as source:
                print("\n🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
                print("🔄 Processing...")
                text = self.recognizer.recognize_google(audio)
                print(f"You: {text}")
                return text.lower()
                
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't catch that")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""
    
    def greet(self):
        """Greet user based on time"""
        hour = datetime.datetime.now().hour
        if hour < 12:
            return "Good morning!"
        elif hour < 18:
            return "Good afternoon!"
        else:
            return "Good evening!"
    
    def get_time(self):
        """Get current time"""
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        return f"The time is {time_str}"
    
    def get_date(self):
        """Get current date"""
        now = datetime.datetime.now()
        date_str = now.strftime("%B %d, %Y, %A")
        return f"Today is {date_str}"
    
    def create_file(self, filename):
        """Create a file on desktop"""
        try:
            desktop = Path.home() / "Desktop"
            if not filename.endswith('.txt'):
                filename += '.txt'
            
            filepath = desktop / filename
            with open(filepath, 'w') as f:
                f.write(f"Created by {self.name}\n")
                f.write(f"Date: {datetime.datetime.now()}\n")
            
            return f"File {filename} created on desktop"
        except Exception as e:
            return f"Could not create file: {str(e)}"
    
    def create_folder(self, foldername):
        """Create a folder on desktop"""
        try:
            desktop = Path.home() / "Desktop"
            folderpath = desktop / foldername
            os.makedirs(folderpath, exist_ok=True)
            return f"Folder {foldername} created on desktop"
        except Exception as e:
            return f"Could not create folder: {str(e)}"
    
    def open_application(self, app_name):
        """Open applications"""
        try:
            system = platform.system()
            app_name = app_name.lower()
            
            if 'notepad' in app_name:
                if system == 'Windows':
                    subprocess.Popen('notepad.exe')
                elif system == 'Darwin':
                    subprocess.Popen(['open', '-a', 'TextEdit'])
                else:
                    subprocess.Popen(['gedit'])
                return "Opening notepad"
            
            elif 'calculator' in app_name:
                if system == 'Windows':
                    subprocess.Popen('calc.exe')
                elif system == 'Darwin':
                    subprocess.Popen(['open', '-a', 'Calculator'])
                else:
                    subprocess.Popen(['gnome-calculator'])
                return "Opening calculator"
            
            elif 'browser' in app_name or 'chrome' in app_name:
                webbrowser.open('https://www.google.com')
                return "Opening browser"
            
            elif 'youtube' in app_name:
                webbrowser.open('https://www.youtube.com')
                return "Opening YouTube"
            
            else:
                return f"I don't know how to open {app_name}"
        except Exception as e:
            return f"Could not open application: {str(e)}"
    
    def search_google(self, query):
        """Search on Google"""
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Searching Google for {query}"
    
    def get_battery(self):
        """Get battery status"""
        try:
            battery = psutil.sensors_battery()
            if battery:
                percent = battery.percent
                plugged = "Plugged in" if battery.power_plugged else "On battery"
                return f"Battery is at {percent}%. {plugged}"
            return "Battery information not available"
        except:
            return "Could not get battery status"
    
    def process_command(self, command):
        """Process user commands"""
        
        # Greetings
        if any(word in command for word in ['hello', 'hi', 'hey']):
            return self.greet() + " How can I help you?"
        
        # Time
        elif 'time' in command:
            return self.get_time()
        
        # Date
        elif 'date' in command or 'day' in command:
            return self.get_date()
        
        # Create file
        elif 'create file' in command or 'make file' in command:
            words = command.split()
            filename = "document"
            if 'named' in command or 'called' in command:
                try:
                    idx = words.index('named') if 'named' in words else words.index('called')
                    filename = '_'.join(words[idx+1:])
                except:
                    pass
            return self.create_file(filename)
        
        # Create folder
        elif 'create folder' in command or 'make folder' in command:
            words = command.split()
            foldername = "new_folder"
            if 'named' in command or 'called' in command:
                try:
                    idx = words.index('named') if 'named' in words else words.index('called')
                    foldername = '_'.join(words[idx+1:])
                except:
                    pass
            return self.create_folder(foldername)
        
        # Open application
        elif 'open' in command:
            app = command.replace('open', '').strip()
            return self.open_application(app)
        
        # Search
        elif 'search' in command or 'google' in command:
            query = command.replace('search', '').replace('google', '').replace('for', '').strip()
            return self.search_google(query)
        
        # Battery
        elif 'battery' in command:
            return self.get_battery()
        
        # Who are you
        elif 'your name' in command or 'who are you' in command:
            return f"I am {self.name}, your AI desktop assistant!"
        
        # Exit
        elif any(word in command for word in ['exit', 'quit', 'bye', 'goodbye']):
            return "exit"
        
        # Help
        elif 'help' in command:
            return """I can help you with:
            - Tell time and date
            - Create files and folders
            - Open applications
            - Search the web
            - Check battery status
            Say 'exit' to quit"""
        
        # AI Feature
        elif self.ai_enabled:
            # Fall back to AI for unknown commands
            try:
                return self.ai_brain.think(command)
            except:
                return "I'm not sure how to help with that. Say 'help' to see what I can do."
        
        # Unknown
        else:
            return "I'm not sure how to help with that. Say 'help' to see what I can do."
    
    def run(self):
        """Main loop"""
        self.speak(f"Hello! I am {self.name}, your desktop assistant. How can I help you?")
        
        while True:
            command = self.listen()
            
            if command:
                response = self.process_command(command)
                
                if response == "exit":
                    self.speak("Goodbye! Have a great day!")
                    break
                
                self.speak(response)

if __name__ == "__main__":
    print("="*50)
    print("     AI DESKTOP ASSISTANT")
    print("="*50)
    assistant = VoiceAssistant()
    assistant.run()

