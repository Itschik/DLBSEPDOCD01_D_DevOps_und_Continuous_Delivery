from django.test import TestCase
from catalog.models import Product

class ProductModelTest(TestCase):
    def test_str(self):
        p = Product.objects.create(name="Test", price=10, stock=5)
        self.assertEqual(str(p), "Test")
