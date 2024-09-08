# Create your tests here.
from django.test import TestCase, Client
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/banban/')
        self.assertEqual(response.status_code, 404)

    def test_in_stock_item(self):
        item = Product.objects.create(
            name="Black Forest Cake",
            price = 40000,
            description = "A Black Forest Cake, also known as a Black Forest gateau, is a sweet tasting cake that consists of \
many layers of chocolate sponge cake, cherry filling, and whipped cream lashings in-between layers.",
            category = "Cake",
            quantity = 5,
        )
        self.assertTrue(item.is_in_stock)