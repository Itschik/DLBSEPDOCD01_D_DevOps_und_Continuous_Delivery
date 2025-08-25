from django.test import TestCase
from django.urls import reverse
from catalog.models import Product
from django.contrib.auth.models import User

class CatalogIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.product = Product.objects.create(name="Testprodukt", price=9.99, description="Testbeschreibung")

    def test_product_catalog_and_cart(self):
        # Schritt 1: Produkt im Katalog anzeigen
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Testprodukt")

        # Schritt 2: Login
        self.client.login(username="testuser", password="12345")

        # Schritt 3: Produkt in Warenkorb legen
        response = self.client.post(reverse("cart:add_to_cart", args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  # Redirect nach Cart

        # Schritt 4: Warenkorb prüfen
        response = self.client.get(reverse("cart:view_cart"))
        self.assertContains(response, "Testprodukt")
