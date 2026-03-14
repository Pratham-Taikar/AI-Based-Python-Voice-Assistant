# 🚀 AI Desktop Assistant - Setup Instructions

## Quick Setup Guide

### Step 1: Install Python
- Download Python 3.11+ from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation
- Verify installation: `python --version`

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Setup API Keys (Optional but Recommended)
1. Copy `.env.template` to `.env`
2. Get OpenAI API key from https://platform.openai.com/api-keys
3. Paste your API key in `.env` file
4. Save the file

### Step 4: Test Microphone
```bash
python test_mic.py
```
If microphone works, proceed to next step.

### Step 5: Run the Application

#### Option A: GUI Version (Recommended)
```bash
python gui_assistant.py
```

#### Option B: Command Line Version
```bash
python assistant.py
```

## Installation Issues?

### Windows: PyAudio Installation
If `pip install pyaudio` fails, try:
```bash
pip install pipwin
pipwin install pyaudio
```

### Linux: Install Tesseract OCR
```bash
sudo apt-get install tesseract-ocr
```

### macOS: Install Tesseract
```bash
brew install tesseract
```

## First Time Setup Checklist

- [ ] Python 3.11+ installed
- [ ] Dependencies installed
- [ ] Microphone working (test_mic.py)
- [ ] API key configured (.env file)
- [ ] Application runs successfully
- [ ] GUI opens correctly
- [ ] Voice recognition works

## Common Commands to Test

1. "What time is it?"
2. "Hello"
3. "Open notepad"
4. "Create file named test"
5. "Battery status"

## Getting Help

1. Check README.md for features
2. Read USER_MANUAL.md for detailed guide
3. Run `python test_mic.py` to troubleshoot microphone
4. Check logs folder for error messages

## Next Steps

1. Explore all features
2. Customize voice shortcuts
3. Setup reminders
4. Try AI conversations
5. Build executable with `python build_script.py`

## Enjoy Your AI Assistant! 🤖

