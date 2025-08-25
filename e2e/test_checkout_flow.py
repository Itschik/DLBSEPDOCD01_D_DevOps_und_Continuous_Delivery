import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from catalog.models import Product
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutFlowE2ETest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()  # ChromeDriver muss installiert sein!

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        self.user = User.objects.create_user(username="e2euser", password="12345")
        self.product = Product.objects.create(
            name="Laptop",
            price=999.99,
            description="High-End Laptop",
            stock=5
        )

    def debug_print(self, step):
        """Hilfsfunktion: zeigt den HTML-Quelltext (gekürzt) an"""
        print(f"\n--- DEBUG: {step} ---")
        html = self.browser.page_source
        print(html[:1000])  # nur die ersten 1000 Zeichen ausgeben
        buttons = self.browser.find_elements(By.TAG_NAME, "button")
        print("Gefundene Buttons:", [b.text for b in buttons])

    def test_full_checkout_flow(self):
        # 1. Katalog aufrufen
        self.browser.get(f"{self.live_server_url}/")
        self.debug_print("Katalog")
        assert "Laptop" in self.browser.page_source

        # 2. Login
        self.browser.get(f"{self.live_server_url}/accounts/login/")
        self.debug_print("Login-Seite")

        self.browser.find_element(By.NAME, "username").send_keys("e2euser")
        self.browser.find_element(By.NAME, "password").send_keys("12345")

        login_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )
        print("Login-Button gefunden:", login_button.text)
        login_button.click()

        # Warten bis Redirect abgeschlossen ist
        WebDriverWait(self.browser, 10).until(
            EC.url_contains(self.live_server_url)
        )
        self.debug_print("Nach Login")

        # 3. Produktseite öffnen
        self.browser.get(f"{self.live_server_url}/product/{self.product.id}/") # Hier wurde product/ hinzugefügt
        self.debug_print("Produktseite")

        add_to_cart_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "In den Warenkorb")]'))
        )
        print("Warenkorb-Button gefunden:", add_to_cart_button.text)
        add_to_cart_button.click()

        # 4. Warenkorb prüfen
        self.browser.get(f"{self.live_server_url}/cart/")
        self.debug_print("Warenkorb")
        assert "Laptop" in self.browser.page_source
