from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Generator for phone numbers
def number_generator():
    for i in range(100_000_000):  # from 0600000000 to 0699999999
        yield f"06{i:08d}"

# Send messages to WhatsApp numbers
def send_messages(message, max_messages=3):
    options = Options()
    
    # Use existing user profile
    options.add_argument(r'--user-data-dir=C:\Users\sao\AppData\Local\Google\Chrome\User Data')
    options.add_argument('--profile-directory=AutomationProfile')  # Use correct profile name
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Load WhatsApp Web first to ensure profile is active
        driver.get("https://web.whatsapp.com")
        print("📱 Waiting for WhatsApp Web to load...")

        # Wait for main UI to load
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
                # Wait for chat input to appear
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
    msg = "Hello from your assistant Nizar 🚀"
    send_messages(msg, max_messages=3)
