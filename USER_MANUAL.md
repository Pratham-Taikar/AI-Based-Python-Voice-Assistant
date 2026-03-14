# 📚 AI Desktop Assistant - User Manual

## Table of Contents
1. [Installation](#installation)
2. [Getting Started](#getting-started)
3. [Voice Commands](#voice-commands)
4. [Features](#features)
5. [Settings](#settings)
6. [Troubleshooting](#troubleshooting)

## Installation

### Windows
1. Download `AI_Assistant_Setup.exe`
2. Double-click to run installer
3. Follow on-screen instructions
4. Launch from desktop shortcut

### Manual Installation
1. Install Python 3.11+
2. Clone/download project
3. Run: `pip install -r requirements.txt`
4. Run: `python gui_assistant.py`

## Getting Started

### First Launch
1. Click the desktop icon
2. Grant microphone permissions
3. Wait for "Ready" status
4. Click "Listen" or type command

### Interface Overview
- **Status Indicator:** Shows assistant state
- **Chat Area:** Conversation history
- **Text Input:** Type commands here
- **Listen Button:** Activate voice mode
- **Quick Actions:** One-click commands

## Voice Commands

### Basic Information
"What time is it?"
"What's the date?"
"What day is today?"
"Battery status"

### File Management
"Create file named report"
"Make folder called projects"
"Create file named todo.txt"

### Application Control
"Open notepad"
"Open calculator"
"Open browser"
"Open YouTube"

### Web Search
"Search for Python tutorials"
"Google machine learning"
"Search YouTube for music"

### Productivity
"Focus for 25 minutes on coding"
"Start focus mode"
"Focus status"
"Stop focus"
"Remind me to submit assignment in 30 minutes"
"Show reminders"
"Clear reminders"

### Voice Shortcuts
"Study mode"
"Work mode"
"List shortcuts"

### Screenshot
"Read my screen"
"Take screenshot"
"Save screenshot"

### AI Conversation
"Tell me a joke"
"Explain Python"
"What is machine learning?"
"Help me with homework"

### System Commands
"Help" - Show help
"Exit" - Close assistant

## Features

### 1. Focus Mode (Pomodoro)
- Set focused work sessions
- Get 5-minute warnings
- Track completed sessions
- Example: "Focus for 25 minutes on studying"

### 2. Smart Reminders
- Set timed reminders
- Get notifications
- View pending reminders
- Example: "Remind me in 1 hour"

### 3. Voice Shortcuts
- Create custom command sequences
- Execute multiple commands at once
- Default shortcuts: study mode, work mode
- Example: "Study mode" opens apps + starts focus

### 4. Screenshot Analysis
- Capture screen
- Extract text using OCR
- Save screenshots
- Example: "Read my screen"

### 5. AI Conversations
- Ask any question
- Get intelligent responses
- Context-aware replies
- Powered by OpenAI GPT

## Settings

### Voice Settings
- Adjust speech rate in config.json
- Change voice volume
- Select different voices

### Appearance
- Dark/Light theme
- Window size customization
- Font size adjustment

### AI Settings
- Enable/disable AI features
- Set conversation history limit
- Configure API preferences

## Troubleshooting

### Microphone Not Working
1. Check microphone is plugged in
2. Grant microphone permissions
3. Test with "test_mic.py"
4. Restart application

### Voice Not Recognized
1. Speak clearly and slowly
2. Reduce background noise
3. Check internet connection
4. Try text input instead

### Application Crashes
1. Check logs folder
2. Update dependencies
3. Reinstall application
4. Contact support

### AI Not Responding
1. Check .env file for API key
2. Verify internet connection
3. Check API quota/billing
4. Use offline features

### Commands Not Working
1. Say "help" for command list
2. Check pronunciation
3. Try alternative phrasing
4. Use text input to verify

## Tips & Tricks

1. **Quick Commands:** Use quick action buttons
2. **Text Mode:** Type when voice isn't working
3. **Shortcuts:** Create custom workflows
4. **Focus:** Use for productivity boost
5. **History:** Review chat for past responses

## Keyboard Shortcuts

- `Enter` - Send typed command
- `Ctrl+C` - Stop listening
- `Esc` - Close application

## Updates

The application checks for updates on startup.
Download latest version from [your website].

## Support

**Email:** your.email@example.com  
**Issues:** GitHub Issues page  
**FAQ:** Check project wiki

## Credits

Developed by [Your Name]  
Powered by OpenAI, Python, and open-source libraries

---

**Version:** 1.0.0  
**Last Updated:** [Date]

