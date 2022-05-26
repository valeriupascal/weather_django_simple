from django.urls import path
from . import views
from .views import CityDelete

urlpatterns = [
    path('', views.index),
    path('del/<int:pk>/', CityDelete.as_view(), name='city-delete'),
]
