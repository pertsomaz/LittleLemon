from restaurant.models import Menu
from django.test import TestCase
from decimal import Decimal

class MenuTest(TestCase):
    
    def test_get_item(self):
        item = Menu.objects.create(Title="Ice Cream", Price=7, Inventory=100)
        self.assertEqual(str(item), "Ice Cream : 7")
    