import subprocess
import os

def main():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    user_data_dir = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data")
    profile_name = "AutomationProfile"

    try:
        subprocess.Popen([
            chrome_path,
            f"--user-data-dir={user_data_dir}",
            f"--profile-directory={profile_name}"
        ])
        print("🌐 Launched Chrome for manual login.")
        print("⌛ Please log into WhatsApp Web and Google in this window.")
        print("After finishing, close Chrome completely.")
        input("✅ Press Enter here after you have logged in and closed Chrome...")
    except Exception as e:
        print(f"❌ Failed to launch Chrome: {e}")

if __name__ == "__main__":
    main()
