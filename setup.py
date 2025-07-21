import os
import subprocess
import sys
import shutil

def is_admin():
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_powershell(command):
    """Run PowerShell command with admin rights"""
    completed = subprocess.run(
        ["powershell", "-Command", command],
        capture_output=True,
        text=True,
        shell=True,
    )
    print(completed.stdout)
    if completed.returncode != 0:
        print("Error running PowerShell command:")
        print(completed.stderr)
        sys.exit(1)

def install_chocolatey():
    choco_check = shutil.which("choco")
    if choco_check:
        print("Chocolatey already installed.")
        return
    print("Installing Chocolatey...")
    ps_cmd = """Set-ExecutionPolicy Bypass -Scope Process -Force;
                [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
                iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"""
    run_powershell(ps_cmd)
    print("Chocolatey installed.")

def install_choco_package(package):
    if shutil.which(package):
        print(f"{package} is already installed.")
        return
    print(f"Installing {package} via Chocolatey...")
    run_powershell(f"choco install {package} -y")

def install_python_packages():
    print("Installing required Python packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium", "webdriver-manager"])

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
    if not is_admin():
        print("Please run this script as Administrator (right-click -> Run as Administrator).")
        sys.exit(1)

    install_chocolatey()
    install_choco_package("git")
    install_choco_package("python")

    install_python_packages()
    profile_path = create_chrome_profile_folder()
    launch_chrome_with_profile(profile_path)
    print("\nSetup complete! You can now run your automation script.")

if __name__ == "__main__":
    main()
