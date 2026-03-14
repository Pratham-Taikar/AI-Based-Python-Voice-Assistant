"""
Test AI Integration
Tests if AI brain is working correctly
"""

print("="*50)
print("AI INTEGRATION TEST")
print("="*50)

# Test 1: Check imports
print("\n1. Testing imports...")
try:
    from modules.ai_brain import AIBrain
    print("✓ AI brain module imported")
except Exception as e:
    print(f"✗ Failed to import AI brain: {e}")
    exit()

# Test 2: Check API Key in Config
print("\n2. Checking Groq API key in config...")
try:
    from config import Config
    conf = Config()
    api_key = conf.get("api_key", "")
    if api_key and api_key != "sk-your-openai-key-here" and api_key.strip() != "":
        print("✓ Groq API key found in config")
    else:
        print("✗ Groq API key not configured or still placeholder")
        print("  → Get your key from: https://console.groq.com/ and add in the app GUI or config")
        exit()
except Exception as e:
    print(f"✗ Failed to access config: {e}")
    exit()

# Test 3: Try to initialize AI brain
print("\n3. Testing AI brain initialization...")
try:
    brain = AIBrain()
    print("✓ AI Brain initialized successfully!")
    
    # Test 4: Try to get AI response
    print("\n4. Testing AI response...")
    print("Asking: 'What is Python?'")
    response = brain.think("What is Python?")
    print(f"✓ AI Response: {response}")
    print("\n" + "="*50)
    print("✓✓✓ AI IS WORKING! ✓✓✓")
    print("="*50)
    
except Exception as e:
    print(f"✗ Failed to initialize AI brain: {e}")
    print("\nPossible issues:")
    print("1. Invalid API key")
    print("2. No internet connection")
    print("3. Rate limit exceeded")
    print("4. API key has no credits")
    exit()

print("\nAI integration is ready! You can now use AI features.")

