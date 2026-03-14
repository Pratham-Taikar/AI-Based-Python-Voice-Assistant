"""
Reminder System Module
Manages timed reminders and notifications
"""

import threading
import time
from datetime import datetime, timedelta
import json
import os

class ReminderSystem:
    def __init__(self, callback=None):
        self.reminders = []
        self.callback = callback
        self.running = False
        self.reminder_file = "reminders.json"
        self.load_reminders()
        self.start_scheduler()
    
    def load_reminders(self):
        """Load reminders"""
        if os.path.exists(self.reminder_file):
            try:
                with open(self.reminder_file, 'r') as f:
                    self.reminders = json.load(f)
            except:
                self.reminders = []
    
    def save_reminders(self):
        """Save reminders"""
        with open(self.reminder_file, 'w') as f:
            json.dump(self.reminders, f, indent=4)
    
    def add_reminder(self, message, minutes_from_now):
        """Add reminder"""
        reminder_time = datetime.now() + timedelta(minutes=minutes_from_now)
        
        reminder = {
            "id": len(self.reminders) + 1,
            "message": message,
            "time": reminder_time.strftime("%Y-%m-%d %H:%M"),
            "completed": False
        }
        
        self.reminders.append(reminder)
        self.save_reminders()
        
        return f"Reminder set for {reminder_time.strftime('%I:%M %p')}"
    
    def check_reminders(self):
        """Check reminders"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        for reminder in self.reminders:
            if not reminder["completed"] and reminder["time"] == current_time:
                reminder["completed"] = True
                if self.callback:
                    self.callback(f"⏰ Reminder: {reminder['message']}")
                self.save_reminders()
    
    def get_all_reminders(self):
        """Get all pending reminders"""
        pending = [r for r in self.reminders if not r["completed"]]
        if pending:
            result = "Pending reminders:\n"
            for r in pending:
                result += f"- {r['time']}: {r['message']}\n"
            return result
        return "No pending reminders"
    
    def start_scheduler(self):
        """Start scheduler"""
        def run():
            self.running = True
            while self.running:
                self.check_reminders()
                time.sleep(30)
        threading.Thread(target=run, daemon=True).start()

