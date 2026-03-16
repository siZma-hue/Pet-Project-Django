from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dine/', views.dine_in),
    path('pickup/', views.pickup_order),
    path('delivery/', views.delivery_order),
]