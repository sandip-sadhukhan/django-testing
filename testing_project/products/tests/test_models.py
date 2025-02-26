from django.core.exceptions import ValidationError
from django.test import TestCase
from products.models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", price=100.00, stock_count=10)
    
    def test_in_stock_property(self):
        self.assertTrue(self.product.in_stock)

        # Set stock_count to 0 test again
        self.product.stock_count = 0
        self.product.save()

        self.assertFalse(self.product.in_stock)
    
    def test_get_discount_price(self):
        self.assertEqual(self.product.get_discounted_price(10), 90)
        self.assertEqual(self.product.get_discounted_price(50), 50)
        self.assertEqual(self.product.get_discounted_price(0), 100)
    
    def test_negative_price_validation(self):
        self.product.price = -10
        self.product.save()

        with self.assertRaises(ValidationError):
            self.product.clean()

    def test_negative_stock_price_validation(self):
        self.product.stock_count = -10
        self.product.save()

        with self.assertRaises(ValidationError):
            self.product.clean()



