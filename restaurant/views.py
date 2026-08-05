from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManager

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


# Menu List (GET, POST)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsManager()]
        return []


# Single Menu Item (GET, PUT, DELETE)
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAuthenticated(), IsManager()]
        return []


# Booking API
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]