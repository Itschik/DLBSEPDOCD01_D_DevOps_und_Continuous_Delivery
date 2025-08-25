from django.test import TestCase
from django.contrib.auth.models import User
from catalog.models import Product
from cart.models import CartItem

class CartItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u", password="p")
        self.product = Product.objects.create(name="P", price=2, stock=10)

    def test_unique_user_product(self):
        CartItem.objects.create(user=self.user, product=self.product, quantity=1)
        # zweites gleicher User+Product erhöht statt Duplikat (simuliert View-Logik)
        item, created = CartItem.objects.get_or_create(user=self.user, product=self.product)
        if not created:
            item.quantity += 1
            item.save()
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(CartItem.objects.first().quantity, 2)
