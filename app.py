from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

def number_generator():
    for i in range(100_000_000):  # 0600000000 to 0699999999
        yield f"06{i:08d}"

def send_messages(message, max_messages=100000000):
    chrome_user_data_dir = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data")
    profile_name = "AutomationProfile"

    options = Options()
    options.add_argument(f'--user-data-dir={chrome_user_data_dir}')
    options.add_argument(f'--profile-directory={profile_name}')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://web.whatsapp.com")
        print("📱 Waiting for WhatsApp Web to load...")

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//div[@title="Search input textbox"]'))
        )
        print("✅ WhatsApp Web loaded successfully.")

        count = 0
        for num in number_generator():
            international_num = "212" + num[1:]  # Moroccan format
            url = f"https://web.whatsapp.com/send?phone={international_num}&text={message}"
            driver.get(url)
            print(f"💬 Opening chat with +{international_num}...")

            try:
                input_box = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @data-tab="10"]'))
                )
                time.sleep(2)
                input_box.send_keys(Keys.ENTER)
                print(f"✅ Message sent to +{international_num}")
            except Exception as e:
                print(f"❌ Failed to send to +{international_num}: {e}")

            count += 1
            if count >= max_messages:
                print("🛑 Reached max message limit.")
                break

            time.sleep(5)
    finally:
        driver.quit()

if __name__ == "__main__":
    print("⚠️ Make sure Chrome is fully closed before running this script.")
    send_messages("Hello from your assistant Nizar 🚀", max_messages=100000000)
