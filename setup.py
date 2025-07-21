from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# ✅ Updated Chrome user profile directory
chrome_user_data_dir = r'C:\Users\sao\AppData\Local\Google\Chrome\User Data'
profile_name = 'NizarWhatsApp'  # custom profile name to isolate from Default

options = Options()
options.add_argument(f'--user-data-dir={chrome_user_data_dir}')
options.add_argument(f'--profile-directory={profile_name}')

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    print("🌐 Opening WhatsApp Web...")
    driver.get("https://web.whatsapp.com")

    print("⌛ Please scan the QR code (if needed) and wait...")
    input("✅ Press Enter after WhatsApp Web is fully loaded...")

finally:
    driver.quit()
