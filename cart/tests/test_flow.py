from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from catalog.models import Product
from cart.models import CartItem

class CartFlowTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="rob", password="secret")
        self.product = Product.objects.create(name="Book", price=9.99, stock=100)

    def test_login_and_add_to_cart(self):
        # Login
        resp = self.client.post(reverse('login'), {'username': 'rob', 'password': 'secret'})
        self.assertEqual(resp.status_code, 302)  # redirect to home

        # Add to cart (POST)
        resp = self.client.post(reverse('add_to_cart', args=[self.product.id]))
        self.assertEqual(resp.status_code, 302)  # redirect to cart_view

        # Cart page shows item
        resp = self.client.get(reverse('cart_view'))
        self.assertContains(resp, "Book")
        self.assertEqual(CartItem.objects.filter(user=self.user, product=self.product).count(), 1)
