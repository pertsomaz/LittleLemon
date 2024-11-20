from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import *
from .serializers import bookingSerializer, menuSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# class bookingview(APIView):
#     def get(self, request):
#         items = booking.objects.all()
#         serializer = bookingSerializer(items, many=True)
#         return Response(serializer.data) 

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer