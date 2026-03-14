"""
API Key Setup Wizard
Helps you configure your API key easily
"""

import os

def setup_api_key():
    """Setup API key interactively"""
    
    print("="*60)
    print("   API KEY SETUP WIZARD")
    print("="*60)
    print("\nThis will help you add your Groq API key to the .env file.")
    key_var = 'GROQ_API_KEY'

    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            pass

    with open('.env', 'r') as f:
        content = f.read()
    
    groq_key_exists = any(line.startswith(key_var+'=') for line in content.splitlines())
    if groq_key_exists:
        print(f"{key_var} already exists in .env. Overwriting...")
        new_content = []
        for line in content.splitlines():
            if line.startswith(key_var+'='):
                new_content.append(f'{key_var}={{api_key}}')
            else:
                new_content.append(line)
        content = '\n'.join(new_content)
    api_key = input("Paste your Groq API key from https://console.groq.com/: ").strip()
    with open('.env', 'w') as f:
        for line in content.splitlines():
            if not line.strip():
                continue
            if line.startswith(key_var+'='):
                f.write(f'{key_var}={api_key}\n')
            else:
                f.write(line + '\n')
        if key_var+'=' not in content:
            f.write(f'\n# Groq API Key\n{key_var}={api_key}\n')
    print(f'✓ Groq API key saved to .env file as {key_var}!')

if __name__ == "__main__":
    try:
        setup_api_key()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
    except Exception as e:
        print(f"\nError: {e}")


