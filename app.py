from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

def number_generator():
    for i in range(100_000_000):  # from 0600000000 to 0699999999
        yield f"06{i:08d}"

def send_messages(message, max_messages=100000000):
    options = Options()
    options.add_argument(r"--user-data-dir=C:\Users\sao\AppData\Local\Google\Chrome\User Data\AutomationProfile")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        count = 0
        for num in number_generator():
            international_num = "212" + num[1:]
            url = f"https://web.whatsapp.com/send?phone={international_num}&text={message}"
            driver.get(url)

            time.sleep(3)  # Give time for page and popup to load

            # Try to find and click invalid number popup OK button
            try:
                # Try multiple possible selectors for the OK button of alert dialog
                possible_ok_buttons = [
                    '//div[@role="alertdialog"]//button[contains(., "OK")]',
                    '//div[@role="alertdialog"]//span[text()="OK"]',
                    '//div[contains(@class,"_2Nr6U")]//span[text()="OK"]',
                    '//div[contains(@class,"_2Nr6U")]//button[contains(., "OK")]',
                ]
                ok_clicked = False
                for xpath in possible_ok_buttons:
                    try:
                        ok_button = WebDriverWait(driver, 2).until(
                            EC.element_to_be_clickable((By.XPATH, xpath))
                        )
                        ok_button.click()
                        ok_clicked = True
                        # print("⚠️ Invalid number popup detected and OK clicked.")  # Debug, can comment out
                        break
                    except TimeoutException:
                        continue
                if ok_clicked:
                    continue  # skip this number and go to next
            except Exception:
                pass  # silently ignore if no popup or error clicking

            # If no popup, continue to send message
            try:
                input_box = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @data-tab="10"]'))
                )
                time.sleep(2)
                input_box.send_keys(Keys.ENTER)
                print(f"✅ Message sent to +{international_num}")
            except Exception:
                # silently skip send errors
                pass

            count += 1
            if count >= max_messages:
                break

            time.sleep(5)

    finally:
        driver.quit()

if __name__ == "__main__":
    print("✅ Make sure Chrome is fully closed before running this script.")
    msg = "Hello from your assistant"
    send_messages(msg, max_messages=100000000)
