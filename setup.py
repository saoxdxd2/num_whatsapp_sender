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

def create_chrome_profile_folder():
    profile_path = r"C:\Users\sao\AppData\Local\Google\Chrome\User Data\AutomationProfile"
    if not os.path.exists(profile_path):
        os.makedirs(profile_path)
        print(f"Created profile folder: {profile_path}")
    else:
        print(f"Profile folder already exists: {profile_path}")
    return profile_path

def launch_chrome_with_profile(profile_path):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        print("Chrome is not installed at the expected path.")
        return

    command = f'"{chrome_path}" --user-data-dir="{profile_path}"'
    print("Launching Chrome with AutomationProfile...")
    subprocess.Popen(command, shell=True)

def main():
    install_packages()
    profile_path = create_chrome_profile_folder()
    launch_chrome_with_profile(profile_path)
    print("\nSetup complete! You can now run your automation script.")

if __name__ == "__main__":
    main()
