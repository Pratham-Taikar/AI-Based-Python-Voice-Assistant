"""
Screenshot Analyzer Module
Captures screenshots and extracts text using OCR
"""

from PIL import ImageGrab
import pytesseract
import os
from pathlib import Path

# Set tesseract path (Windows only)
if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ScreenshotAnalyzer:
    def __init__(self):
        self.last_screenshot = None
    
    def capture_screen(self):
        """Capture screenshot"""
        try:
            screenshot = ImageGrab.grab()
            self.last_screenshot = screenshot
            return screenshot
        except Exception as e:
            return None
    
    def extract_text(self, image=None):
        """Extract text using OCR"""
        try:
            if image is None:
                image = self.capture_screen()
            
            if image:
                text = pytesseract.image_to_string(image)
                return text.strip()
            return "Could not capture screen"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def read_screen(self):
        """Read screen text"""
        text = self.extract_text()
        if text:
            if len(text) > 500:
                text = text[:500] + "..."
            return f"Screen text: {text}"
        return "No text found"
    
    def save_screenshot(self, filename="screenshot.png"):
        """Save screenshot"""
        try:
            desktop = Path.home() / "Desktop"
            filepath = desktop / filename
            
            screenshot = self.capture_screen()
            if screenshot:
                screenshot.save(filepath)
                return f"Screenshot saved as {filename}"
            return "Could not capture"
        except Exception as e:
            return f"Error: {str(e)}"

