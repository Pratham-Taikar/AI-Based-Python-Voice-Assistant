# 🚀 AI Desktop Assistant - Quick Start Guide

## ⚡ Installation in 3 Steps

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

**Note:** If `pyaudio` installation fails on Windows, use:
```bash
pip install pipwin
pipwin install pyaudio
```

### 2️⃣ Configure API Key (Optional but Recommended)
1. Copy `.env.template` to `.env`
2. Get your OpenAI API key from https://platform.openai.com/api-keys
3. Replace `sk-your-openai-key-here` with your actual key
4. Save the file

### 3️⃣ Test and Run

**Test your microphone:**
```bash
python test_mic.py
```

**Run the GUI version:**
```bash
python gui_assistant.py
```

**Run the command-line version:**
```bash
python assistant.py
```

## 🎤 First Commands to Try

Try these voice or text commands:

1. **"Hello"** - Test basic functionality
2. **"What time is it?"** - Get current time
3. **"Create file named test"** - Create a file on desktop
4. **"Open notepad"** - Open notepad
5. **"Battery status"** - Check battery level

## 📋 Features Available

✅ Voice Recognition
✅ Text-to-Speech  
✅ File & Folder Creation
✅ Application Control
✅ Web Search
✅ Battery Status
✅ AI Conversations (with API key)
✅ Focus Mode
✅ Reminders
✅ Voice Shortcuts
✅ Screenshot Analysis
✅ Modern GUI Interface

## 🔧 Troubleshooting

### Microphone Not Working?
```bash
python test_mic.py
```
- Check microphone is plugged in
- Grant microphone permissions
- Speak clearly and reduce background noise

### Import Errors?
```bash
pip install --upgrade -r requirements.txt
```

### GUI Not Showing?
```bash
pip install customtkinter --upgrade
```

### AI Features Not Working?
- Check if `.env` file exists
- Verify API key is correct
- Check internet connection
- Review logs folder for errors

## 📁 Project Files

- **assistant.py** - Main assistant (command line)
- **gui_assistant.py** - GUI version (recommended)
- **test_mic.py** - Microphone tester
- **build_script.py** - Build executable
- **config.py** - Configuration manager
- **modules/** - Feature modules
- **tests/** - Unit tests

## 📚 Documentation

- **README.md** - Project overview
- **USER_MANUAL.md** - Complete user guide
- **SETUP_INSTRUCTIONS.md** - Detailed setup
- **PROJECT_STRUCTURE.md** - File structure

## 🎯 Next Steps

1. ✅ Install dependencies
2. ✅ Configure API key
3. ✅ Test microphone
4. ✅ Run the application
5. ✅ Try all features
6. ✅ Customize settings
7. ✅ Build executable (optional)

## 💡 Tips

- Use **"Help"** command to see all available commands
- Type commands or speak them - both work!
- Check logs folder for debugging info
- Create custom shortcuts for your workflow
- Use focus mode for productivity
- Enable AI for intelligent conversations

## 🎉 You're All Set!

Your AI Desktop Assistant is ready to use. Have fun exploring all the features!

For detailed information, check the README.md and USER_MANUAL.md files.

---

**Questions? Issues?** Check the troubleshooting section above or review the documentation files.

