"""
Logger Module
Handles application logging for debugging and monitoring
"""

import logging
from datetime import datetime
import os

class Logger:
    def __init__(self):
        # Create logs directory
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        # Setup logging
        log_file = f"logs/assistant_{datetime.now().strftime('%Y%m%d')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger(__name__)
    
    def info(self, message):
        """Log info"""
        self.logger.info(message)
    
    def error(self, message):
        """Log error"""
        self.logger.error(message)
    
    def warning(self, message):
        """Log warning"""
        self.logger.warning(message)
    
    def debug(self, message):
        """Log debug"""
        self.logger.debug(message)

