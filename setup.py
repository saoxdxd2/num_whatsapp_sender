import os
import subprocess
import sys
import time
import shutil

# Required Python packages
REQUIRED_PACKAGES = [
    'selenium',
    'webdriver-manager'
]

def install_packages():
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", *REQUIRED_PACKAGES])

def create_chrome_profile_folder():
    profile_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\AutomationProfile")
    if not os.path.exists(profile_path):
        os.makedirs(profile_path)
        print(f"Created profile folder: {profile_path}")
    else:
        print(f"Profile folder already exists: {profile_path}")
    return profile_path

def launch_chrome_with_profile(profile_path):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if not os.path.isfile(chrome_path):
        print("Chrome is not installed at the expected path.")
        return

    print("Launching Chrome with AutomationProfile...")
    try:
        subprocess.Popen([
            chrome_path,
            f'--user-data-dir={profile_path}',
            '--no-first-run',
            '--no-default-browser-check'
        ])
        print("Chrome launched. Please log into your Google account in the opened window.")
    except Exception as e:
        print(f"Failed to launch Chrome: {e}")

def main():
    install_packages()
    profile_path = create_chrome_profile_folder()
    launch_chrome_with_profile(profile_path)
    print("\nSetup complete! You can now run your automation script.")

if __name__ == "__main__":
    main()
