from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import *
from .serializers import bookingSerializer, menuSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
