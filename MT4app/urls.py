from . import views
from django.urls import path

urlpatterns = [
    path('', views.welcome, name='home'),
    path('services', views.services, name='services'),
]