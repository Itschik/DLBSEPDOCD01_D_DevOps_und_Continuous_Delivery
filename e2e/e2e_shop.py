from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

# Pfad zum Chromedriver, falls nötig:
service = Service(r"C:\Users\robin\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome()  # wenn Selenium 4.25+ mit Auto-Driver

base = "http://127.0.0.1:8000/"
driver.get(base)

def wait(by, val, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, val)))

# Registrieren (einfacher Flow)
driver.get(base + "accounts/register/")
wait(By.NAME, "username").send_keys("selenium")
wait(By.NAME, "password").send_keys("secret123")
wait(By.CSS_SELECTOR, "button[type='submit']").click()

# Produkt anklicken (erwarte, dass mindestens 1 Produkt existiert)
wait(By.CSS_SELECTOR, "ul li a").click()  # erstes Produkt
# In den Warenkorb
wait(By.CSS_SELECTOR, "form button[type='submit']").click()

# Warenkorb prüfen
wait(By.TAG_NAME, "body")
time.sleep(1)  # kurze visuelle Pause
os.makedirs("screenshots", exist_ok=True)
driver.save_screenshot(os.path.join("screenshots", "cart.png"))
driver.quit()
