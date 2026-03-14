# 🤖 AI Feature Troubleshooting Guide

## Why AI Features Aren't Working

### 🔍 Problem: AI features are disabled

**Check:** Look at console output when starting the app:
- If you see: `✓ AI Brain activated!` → AI is working ✅
- If you DON'T see this message → AI is disabled ❌

## ✅ Solutions

### Solution 1: Create .env File

**Step 1:** Create `.env` file in project root
```bash
# In project root (C:\college\EDI Final)
Copy-Item .env.template .env
```

**Step 2:** Get Groq API Key
- Go to: https://console.groq.com/
- Sign up or log in
- Click "Create new secret key"
- Copy the key (starts with `sk-`)

**Step 3:** Edit .env file
```bash
# Open .env and replace this:
GROQ_API_KEY=sk-your-groq-key-here

# With your actual key:
GROQ_API_KEY=sk-proj-abc123xyz789...
```

**Step 4:** Restart the application

### Solution 2: Free API Key Alternative

**Option A: Use Groq (Has Free Tier)**
- $5 free credit when you sign up
- Enough for testing and development
- Get it at: https://console.groq.com/signup

**Option B: Use Ollama (100% Free, Local)**
- Download: https://ollama.ai
- Run locally without API key
- No internet required
- (Would need code modification)

### Solution 3: Check if Dependencies are Installed

```bash
# Install required packages
pip install openai python-dotenv

# Or install all
pip install -r requirements.txt
```

## 🔧 Diagnostic Commands

### Test 1: Check .env File Exists
```bash
Test-Path .env
```
Should return: `True`

### Test 2: Check API Key in .env
```bash
Get-Content .env | Select-String "GROQ_API_KEY"
```
Should show your actual key (not the template)

### Test 3: Test AI Import
```python
# Run this in Python
from modules.ai_brain import AIBrain
brain = AIBrain()
print("AI Brain working!")
```

### Test 4: Check Error Logs
```bash
Get-Content logs\assistant_*.log
```

## 🎯 What You Should See When Working

### Console Output (Working):
```
Initializing AI Assistant...
✓ Jarvis initialized successfully!
✓ AI Brain activated!  ← THIS LINE MEANS AI IS ON
```

### Console Output (Not Working):
```
Initializing AI Assistant...
✓ Jarvis initialized successfully!
← NO "AI Brain activated" line means AI is OFF
```

## 💡 Current Status of Your Project

### File Status:
✅ `.env` file created (but needs your API key)
✅ AI brain module exists
✅ Integration code is correct
✅ Graceful fallback works (app still runs without AI)

### What You Need:
⚠️ Your Groq API key in .env file

## 📝 Quick Fix Steps

1. **Get API key:**
   - Visit: https://console.groq.com/
   - Create new key (free $5 credit)

2. **Edit .env file:**
   ```bash
   notepad .env
   # Replace the placeholder with your key
   ```

3. **Save and restart:**
   ```bash
   python gui_assistant.py
   ```

4. **Verify AI is working:**
   - Look for "✓ AI Brain activated!" message
   - Try asking: "What is Python?"
   - Should get intelligent AI response

## 🚫 Workaround: Use Without AI

The app **works perfectly** without AI! All these features work:
- ✅ Voice commands
- ✅ File management
- ✅ Application control
- ✅ Web search
- ✅ Battery status
- ✅ Time/date
- ✅ Basic commands

Only **AI conversations** require the API key.

## ⚠️ Common Errors

### Error 1: "Groq API key not configured"
**Fix:** Create .env file and add your API key

### Error 2: "Rate limit exceeded"
**Fix:** You've used your free credits. Get a new API key or upgrade plan

### Error 3: "Invalid API key"
**Fix:** Check that your key is correct. Make sure there are no extra spaces

### Error 4: "Module not found: ai_brain"
**Fix:** Run from project root: `python gui_assistant.py`

## ✅ Test AI Feature

Once configured, test with these commands:
- "What is machine learning?"
- "Explain Python"
- "Tell me a joke"
- "What is artificial intelligence?"

If AI is working, you'll get intelligent responses!
If not working, you'll get: "I'm not sure how to help with that..."

## 📞 Need Help?

1. Check `.env` file has your API key
2. Restart the application
3. Check console output for "AI Brain activated!"
4. Try test command above
5. Check logs folder for errors

