from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views, MenuItemsView, SingleMenuItemView, BookingViewSet

router = DefaultRouter()
router.register(r'booking',views.BookingViewSet)

urlpatterns = [
    path("menu/", views.MenuItemsView.as_view(), name="menu-items"),
    path("menu/<int:pk>/", views.SingleMenuItemView.as_view(), name="single-menu-item"),
    path("booking/", include(router.urls)),
]