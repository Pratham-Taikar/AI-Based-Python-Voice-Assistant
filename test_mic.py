import speech_recognition as sr

print("Testing microphone...")
r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("✓ Microphone found!")
        print("Adjusting for ambient noise... Please wait")
        r.adjust_for_ambient_noise(source, duration=2)
        print("Say something!")
        audio = r.listen(source, timeout=5)
        print("Processing...")
        
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        print("✓ Microphone working perfectly!")
        
except sr.WaitTimeoutError:
    print("✗ No speech detected. Check your microphone.")
except sr.UnknownValueError:
    print("✗ Could not understand audio. Try again.")
except sr.RequestError as e:
    print(f"✗ Could not request results; {e}")
except Exception as e:
    print(f"✗ Error: {e}")

