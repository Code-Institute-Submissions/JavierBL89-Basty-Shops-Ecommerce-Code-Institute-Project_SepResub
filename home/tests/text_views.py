from django.test import TestCase
from products.models import Product
from django.shortcuts import redirect, reverse
from django.contrib.auth.models import User


class TestHomeView(TestCase):
    """
    Class to test home page view
    """
    def test_home(self):
        """
        Test home page view
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')


class TestProductsView(TestCase):
    """
    Class to test products page view
    """
    def test_products_page(self):
        """
        Test products page view
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')


class TestProductDetailsView(TestCase):
    """
    Class to test product details view
    """
    def test_product_details_page(self):
        """
        Test product details view
        """
        product = Product.objects.create(name='test',
                                         title="test",
                                         sku=582456,
                                         description='test',
                                         price=0.00)
        response = self.client.get(f'/products/{product.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')


class TestBagView(TestCase):
    """
    Class to test bag view
    """
    def test_bag_page(self):
        """
        Test bag view
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')


class TestCheckoutView(TestCase):
    """
    Class to checkout view
    """
    def test_checkout_page(self):
        """
        Test checkout view
        """
        response = self.client.get('/checkout/', follow=True)
        self.assertEqual(response.status_code, 200)


class TestAddProductView(TestCase):
    """
    Class to add product view
    """
    def test_add_product_page(self):
        """
        Test add product view
        """
        response = self.client.get('/products/add/', follow=True)
        self.assertEqual(response.status_code, 200)


class TestEditProductView(TestCase):
    """
    Class to edit product view
    """
    def test_edit_product_page(self):
        """
        Test edit product view
        """
        product = Product.objects.create(name='test',
                                         title="test",
                                         sku=582456,
                                         description='test',
                                         price=0.00)
        response = self.client.get(f'/products/edit/{product.id}', follow=True)
        self.assertEqual(response.status_code, 200)


class LoginTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('javier', 'lennon@thebeatles.com', 'javierpassword')

    def testLogin(self):
        self.client.login(email='javier', password='javierpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)





