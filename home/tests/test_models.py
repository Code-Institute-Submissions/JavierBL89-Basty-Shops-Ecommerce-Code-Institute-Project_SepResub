from django.test import TestCase

from products.models import Product


class TestProducModel(TestCase):

    def setUp(self):
        product = Product.objects.create(name='KAMIRA',
                                         title='Shoes',
                                         sku='hg8554611',
                                         description='must wear everywhere',
                                         price=25.50)

    def test_product(self):
        product = Product.objects.get(name="KAMIRA")
        self.assertTrue(product)
        self.assertEqual(product.title, 'Shoes')
