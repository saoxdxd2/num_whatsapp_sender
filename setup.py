from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Use the custom AutomationProfile folder inside Chrome User Data
chrome_user_data_dir = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data")
profile_name = "AutomationProfile"

options = Options()
options.add_argument(f'--user-data-dir={chrome_user_data_dir}')
options.add_argument(f'--profile-directory={profile_name}')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    print("🌐 Opening WhatsApp Web...")
    driver.get("https://web.whatsapp.com")
    print("⌛ Please scan the QR code and log in if needed.")
    input("✅ Press Enter after you have fully logged in and WhatsApp Web is ready...")
finally:
    driver.quit()
