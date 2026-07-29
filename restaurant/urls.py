from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemsView, SingleMenuItemView, BookingViewSet

router = DefaultRouter()
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path("menu/", MenuItemsView.as_view(), name="menu-items"),
    path("menu/<int:pk>/", SingleMenuItemView.as_view(), name="single-menu-item"),
    path("", include(router.urls)),
]