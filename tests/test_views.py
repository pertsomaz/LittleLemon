from restaurant.models import Menu
from django.test import TestCase
from restaurant.serializers import menuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status




class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(Title="Pizza", Price=12.00, Inventory=10)
        self.item2 = Menu.objects.create(Title="Pasta", Price=8, Inventory=20)
        self.item3 = Menu.objects.create(Title="Pita", Price=4, Inventory=15)
        
    
    def test_getall(self):
        # GET request to retrieve all menu items
        response = self.client.get(reverse('menu'))
        
        items = Menu.objects.all()
        serializer_class = menuSerializer(items, many=True)
        
        self.assertEqual(response.data, serializer_class.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        