from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Menu Items View (GET all items, POST new item)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Single Menu Item View (GET, PUT, DELETE single item by ID)
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer