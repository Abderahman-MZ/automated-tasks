"""
open_chrome_tabs.py
-------------------

This script automates the process of opening multiple URLs in Google Chrome using a specified user profile.

Usage:
    python open_chrome_tabs.py

Dependencies:
    - subprocess (standard library)
    - os (standard library)
"""
import subprocess


# Path to the Chrome executable
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Path to your specific Chrome user profile
user_profile = r"C:\Users\HP_LAPTOP\AppData\Local\Google\Chrome\User Data\Profile 16"

# List of URLs to open
urls = [
    "https://chatgpt.com/",
    "https://chat.deepseek.com/",
    "https://claude.ai/",
    "https://gemini.google.com/app",
    "https://x.com/i/grok",
    "https://www.perplexity.ai/"
]

# Construct the command to open Chrome with the specified profile and URLs
command = [chrome_path, f'--profile-directory=Profile 16'] + urls

# Execute the command
subprocess.Popen(command)
