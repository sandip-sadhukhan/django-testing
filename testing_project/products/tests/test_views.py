from django.test import TestCase, SimpleTestCase
from products.models import Product, User
from django.urls import reverse

class TestProfilePage(TestCase):
    def test_profile_view_redirects_for_anonymous_users(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, expected_url=f"{reverse('login')}?next={reverse('profile')}")

    def test_profile_view_accessible_for_authenticated_users(self):
        # Create User
        User.objects.create_user(username='testuser', password='password123')

        # Login User
        self.client.login(username='testuser', password='password123')

        response = self.client.get(reverse('profile'))

        self.assertContains(response, 'testuser')


class TestHomePage(SimpleTestCase):
    def test_homepage_uses_correct_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'index.html')

    def test_homepage_contains_welcome_message(self):
        response = self.client.get('/')
        self.assertContains(response, 'Welcome to our Store!')

class TestProductPage(TestCase):
    def setUp(self):
        Product.objects.create(name="Laptop", price=1000, stock_count=5)
        Product.objects.create(name="Phone", price=800, stock_count=10)
    
    def test_products_uses_correct_template(self):
        response = self.client.get(reverse('products'))
        self.assertTemplateUsed(response, 'products.html')
    
    def test_products_context(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(len(response.context['products']), 2)
        self.assertContains(response, "Laptop")
        self.assertContains(response, "Phone")
        self.assertNotContains(response, "No products available")
    
    def test_products_view_no_products(self):
        Product.objects.all().delete()
        response = self.client.get(reverse('products'))

        self.assertEqual(len(response.context['products']), 0)
        self.assertContains(response, "No products available")


        
