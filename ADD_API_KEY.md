# 🔑 How to Add Your API Key

## Option 1: Quick Setup (Easiest! ✨)

Run this wizard:
```bash
python setup_api_key.py
```

It will guide you through the process!

## Option 2: Manual Setup

### Step 1: Get Your API Key

**Free Option:** Groq gives you $5 free credits!
1. Go to: https://console.groq.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-proj-...`)

### Step 2: Add to .env File

**Method A: Using Notepad**
```bash
notepad .env
```

Replace this line:
```
GROQ_API_KEY=sk-your-groq-key-here
```

With your actual key:
```
GROQ_API_KEY=sk-proj-abc123xyz789...
```

Save and close.

**Method B: Using PowerShell**
```bash
$key = Read-Host "Enter your API key"
(Get-Content .env) -replace 'GROQ_API_KEY=.*', "GROQ_API_KEY=$key" | Set-Content .env
```

## Option 3: Use Alternative AI Providers

### Why Not Hardcode Keys?

❌ **NEVER hardcode API keys in source code because:**
- Security risk: Anyone can see your key
- Version control: Keys get committed to Git
- Sharing: Can't share code safely
- Rotation: Can't change keys easily

✅ **Using .env file:**
- Secure: Never committed to Git (in .gitignore)
- Flexible: Easy to change keys
- Private: Each user has their own key
- Professional: Industry best practice

### Alternative AI Providers

If you want to use different AI providers:

#### 1. Anthropic Claude
```bash
# Edit .env
CLAUDE_API_KEY=your-claude-key
```

Then modify `modules/ai_brain.py` to use Claude API.

#### 2. Google Gemini
```bash
# Edit .env
GEMINI_API_KEY=your-gemini-key
```

Then modify `modules/ai_brain.py` to use Gemini API.

#### 3. Local AI (Ollama - FREE!)
```bash
# No API key needed!
# Download: https://ollama.ai
```

#### 4. Continue Without AI
The app works perfectly without AI features!

## 🧪 Test Your Setup

After adding your key:
```bash
python test_ai.py
```

You should see: ✓✓✓ AI IS WORKING!

## 📝 Your .env File

Location: `C:\college\EDI Final\.env`

Contents should look like:
```env
# Groq API Key
GROQ_API_KEY=sk-proj-your-actual-key-here

# Weather API (Optional)
WEATHER_API_KEY=your-weather-api-key
...
```

## ✅ Quick Checklist

- [ ] Got API key from Groq
- [ ] Created/updated .env file
- [ ] Added key to GROQ_API_KEY=
- [ ] Saved the file
- [ ] Ran: `python test_ai.py`
- [ ] It says "AI IS WORKING!"

## 🆘 Still Having Issues?

1. Check .env file exists
2. Check key is on one line (no line breaks)
3. Check key starts with `sk-`
4. Check no extra spaces
5. Try running: `python test_ai.py` for diagnostics

## 💡 Security Tips

1. ✅ Keep .env file private (never share it)
2. ✅ Add .env to .gitignore (already done!)
3. ✅ Don't commit API keys to GitHub
4. ✅ Rotate keys if exposed
5. ✅ Use environment variables

## 🎯 Current Status

Your .env file location:
```
C:\college\EDI Final\.env
```

**Run this to setup:**
```bash
python setup_api_key.py
```

**Or manually edit:**
```bash
notepad .env
```

Add your key and save!


