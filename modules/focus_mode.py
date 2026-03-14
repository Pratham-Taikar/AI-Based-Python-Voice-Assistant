"""
Focus Mode Module
Implements Pomodoro technique for productivity
"""

import time
import threading
from datetime import datetime, timedelta

class FocusMode:
    def __init__(self):
        self.is_active = False
        self.end_time = None
        self.task_name = ""
        self.sessions_completed = 0
    
    def start(self, duration_minutes, task_name, callback=None):
        """Start focus session"""
        self.is_active = True
        self.end_time = datetime.now() + timedelta(minutes=duration_minutes)
        self.task_name = task_name
        self.callback = callback
        
        if callback:
            callback(f"Focus mode: {task_name} for {duration_minutes} minutes")
        
        threading.Thread(target=self._countdown, daemon=True).start()
    
    def _countdown(self):
        """Countdown timer"""
        while datetime.now() < self.end_time and self.is_active:
            time.sleep(60)
            remaining = (self.end_time - datetime.now()).seconds // 60
            
            if remaining == 5 and self.callback:
                self.callback("5 minutes remaining")
        
        if self.is_active:
            self.sessions_completed += 1
            if self.callback:
                self.callback(f"Focus complete! {self.task_name}")
            self.stop()
    
    def stop(self):
        """Stop focus session"""
        self.is_active = False
    
    def get_status(self):
        """Get status"""
        if self.is_active:
            remaining = (self.end_time - datetime.now()).seconds // 60
            return f"Active: {self.task_name} - {remaining} min left"
        return "Not active"

