"""
AI Desktop Assistant - GUI Version
Beautiful graphical interface with CustomTkinter
"""

import customtkinter as ctk
from assistant import VoiceAssistant
import threading
from datetime import datetime

class AssistantGUI:
    def __init__(self):
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create window
        self.root = ctk.CTk()
        self.root.title("AI Desktop Assistant")
        self.root.geometry("600x800")
        
        # Initialize assistant
        self.assistant = VoiceAssistant()
        self.is_listening = False
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup user interface"""
        
        # Header
        header_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=20)
        
        title = ctk.CTkLabel(
            header_frame,
            text="🤖 AI Desktop Assistant",
            font=("Arial", 28, "bold")
        )
        title.pack()
        
        # Status
        self.status_label = ctk.CTkLabel(
            header_frame,
            text="● Ready",
            font=("Arial", 14),
            text_color="green"
        )
        self.status_label.pack(pady=5)
        
        # --- API Key Section ---
        apikey_frame = ctk.CTkFrame(self.root)
        apikey_frame.pack(fill="x", padx=20, pady=(0,10))
        ctk.CTkLabel(
            apikey_frame,
            text="AI API Key:",
            font=("Arial", 12, "bold")
        ).pack(side="left", padx=(5,10))

        self.apikey_entry = ctk.CTkEntry(
            apikey_frame,
            placeholder_text="Paste your API key here...",
            width=300
        )
        self.apikey_entry.pack(side="left", padx=(0,10))
        save_btn = ctk.CTkButton(
            apikey_frame,
            text="Save",
            command=self.save_api_key,
            font=("Arial", 12)
        )
        save_btn.pack(side="left")
        
        # Chat area
        chat_frame = ctk.CTkFrame(self.root)
        chat_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        ctk.CTkLabel(
            chat_frame,
            text="Conversation",
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        
        self.chat_display = ctk.CTkTextbox(
            chat_frame,
            font=("Arial", 12),
            wrap="word"
        )
        self.chat_display.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Input area
        input_frame = ctk.CTkFrame(self.root)
        input_frame.pack(fill="x", padx=20, pady=10)
        
        self.text_input = ctk.CTkEntry(
            input_frame,
            placeholder_text="Type your command or click Listen...",
            font=("Arial", 12),
            height=40
        )
        self.text_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.text_input.bind("<Return>", lambda e: self.send_text_command())
        
        # Buttons
        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack(fill="x", padx=20, pady=10)
        
        self.listen_btn = ctk.CTkButton(
            button_frame,
            text="🎤 Listen",
            command=self.toggle_listening,
            font=("Arial", 14),
            height=40,
            width=150
        )
        self.listen_btn.pack(side="left", padx=5)
        
        self.send_btn = ctk.CTkButton(
            button_frame,
            text="Send",
            command=self.send_text_command,
            font=("Arial", 14),
            height=40,
            width=100
        )
        self.send_btn.pack(side="left", padx=5)
        
        clear_btn = ctk.CTkButton(
            button_frame,
            text="Clear",
            command=self.clear_chat,
            font=("Arial", 14),
            height=40,
            width=100,
            fg_color="gray"
        )
        clear_btn.pack(side="left", padx=5)
        
        # Quick actions
        quick_frame = ctk.CTkFrame(self.root)
        quick_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        ctk.CTkLabel(
            quick_frame,
            text="Quick Actions:",
            font=("Arial", 12, "bold")
        ).pack(pady=5)
        
        quick_btns_frame = ctk.CTkFrame(quick_frame, fg_color="transparent")
        quick_btns_frame.pack(fill="x", padx=10, pady=5)
        
        quick_commands = [
            ("⏰ Time", "what time is it"),
            ("📅 Date", "what's the date"),
            ("🔋 Battery", "battery status"),
            ("❓ Help", "help")
        ]
        
        for text, command in quick_commands:
            btn = ctk.CTkButton(
                quick_btns_frame,
                text=text,
                command=lambda cmd=command: self.execute_command(cmd),
                width=130,
                height=35
            )
            btn.pack(side="left", padx=5)
    
    def add_message(self, sender, message):
        """Add message to chat"""
        timestamp = datetime.now().strftime("%I:%M %p")
        self.chat_display.insert("end", f"[{timestamp}] {sender}: {message}\n\n")
        self.chat_display.see("end")
    
    def toggle_listening(self):
        """Toggle voice listening"""
        if not self.is_listening:
            self.is_listening = True
            self.listen_btn.configure(text="⏹️ Stop", fg_color="red")
            self.status_label.configure(text="● Listening...", text_color="red")
            threading.Thread(target=self.listen_and_respond, daemon=True).start()
        else:
            self.is_listening = False
            self.listen_btn.configure(text="🎤 Listen", fg_color=["#3B8ED0", "#1F6AA5"])
            self.status_label.configure(text="● Ready", text_color="green")
    
    def listen_and_respond(self):
        """Listen and respond"""
        command = self.assistant.listen()
        
        if command and self.is_listening:
            self.add_message("You", command)
            response = self.assistant.process_command(command)
            
            if response != "exit":
                self.add_message("Assistant", response)
                self.assistant.speak(response)
            else:
                self.add_message("Assistant", "Goodbye!")
        
        self.is_listening = False
        self.listen_btn.configure(text="🎤 Listen", fg_color=["#3B8ED0", "#1F6AA5"])
        self.status_label.configure(text="● Ready", text_color="green")
    
    def send_text_command(self):
        """Send text command"""
        command = self.text_input.get().strip()
        if command:
            self.execute_command(command)
            self.text_input.delete(0, "end")
    
    def execute_command(self, command):
        """Execute a command"""
        self.add_message("You", command)
        response = self.assistant.process_command(command.lower())
        self.add_message("Assistant", response)
    
    def clear_chat(self):
        """Clear chat"""
        self.chat_display.delete("1.0", "end")
    
    def save_api_key(self):
        """Save API Key to config file and activate AI services"""
        api_key = self.apikey_entry.get().strip()
        if api_key:
            try:
                from config import Config
                from modules.ai_brain import AIBrain
                conf = Config()
                conf.set("api_key", api_key)
                # Try initializing AI brain (which uses new API key)
                self.assistant.ai_brain = AIBrain()
                self.assistant.ai_enabled = True
                self.status_label.configure(text="● AI Activated!", text_color="green")
            except Exception as e:
                self.status_label.configure(text=f"● Error: {str(e)}", text_color="red")
                self.assistant.ai_enabled = False
        else:
            self.status_label.configure(text="● Enter a valid API key!", text_color="orange")
    
    def run(self):
        """Start GUI"""
        self.add_message("Assistant", "Hello! I'm your AI assistant. Type or speak a command.")
        self.root.mainloop()

if __name__ == "__main__":
    app = AssistantGUI()
    app.run()

