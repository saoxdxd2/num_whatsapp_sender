import os
import subprocess
import sys

# Required Python packages
REQUIRED_PACKAGES = [
    'selenium',
    'webdriver-manager'
]

def install_packages():
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", *REQUIRED_PACKAGES])

def get_existing_chrome_profile_path():
    # Using the 'Default' profile which is already signed-in
    profile_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default")
    
    if os.path.exists(profile_path):
        print(f"Using existing signed-in Chrome profile: {profile_path}")
        return profile_path
    else:
        print("Signed-in Chrome profile not found at expected location.")
        return None

def launch_chrome_with_profile(profile_path):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        print("Chrome is not installed at the expected path.")
        return

    print("Launching Chrome with signed-in profile...")
    try:
        subprocess.Popen([
            chrome_path,
            f'--user-data-dir={os.path.dirname(profile_path)}',
            f'--profile-directory={os.path.basename(profile_path)}'
        ])
    except Exception as e:
        print(f"Failed to launch Chrome: {e}")

def main():
    install_packages()
    profile_path = get_existing_chrome_profile_path()
    if profile_path:
        launch_chrome_with_profile(profile_path)
    else:
        print("Profile not available. Please sign in to Chrome manually first.")
    print("\nSetup complete! You can now run your automation script.")

if __name__ == "__main__":
    main()
