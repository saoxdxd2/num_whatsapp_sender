import subprocess

def main():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    automation_profile_path = r"C:\Users\sao\AppData\Local\Google\Chrome\User Data\AutomationProfile"

    try:
        subprocess.Popen([
            chrome_path,
            f"--user-data-dir={automation_profile_path}"
            # No --profile-directory here because automation_profile_path points directly to profile folder
        ])
        print("🌐 Launched Chrome for manual login.")
        print("⌛ Please log into WhatsApp Web and Google in this window.")
        print("After finishing, close Chrome completely.")
        input("✅ Press Enter here after you have logged in and closed Chrome...")
    except Exception as e:
        print(f"❌ Failed to launch Chrome: {e}")

if __name__ == "__main__":
    main()
