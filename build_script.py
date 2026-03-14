"""
Build Script
Creates executable file using PyInstaller
"""

import PyInstaller.__main__
import os
import sys

def build_executable():
    """Build the executable"""
    
    app_name = "AI_Desktop_Assistant"
    main_file = "gui_assistant.py"
    icon_file = "assets/icon.ico"
    
    # Build arguments
    args = [
        main_file,
        '--name=%s' % app_name,
        '--onefile',
        '--windowed',
        '--add-data=modules;modules',
        '--hidden-import=pyttsx3.drivers',
        '--hidden-import=pyttsx3.drivers.sapi5',
        '--collect-all=customtkinter',
    ]
    
    # Add icon if exists
    if os.path.exists(icon_file):
        args.append('--icon=%s' % icon_file)
    
    print("Building executable...")
    print("This may take a few minutes...")
    
    PyInstaller.__main__.run(args)
    
    print("\n✓ Build complete!")
    print(f"Executable location: dist/{app_name}.exe")

if __name__ == "__main__":
    build_executable()

