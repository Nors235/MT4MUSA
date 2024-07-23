from . import views
from django.urls import path

urlpatterns = [
    path('', views.welcome, name='home'),
    path('services', views.services, name='services'),
    path('reviews', views.ReviewCreateView.as_view(), name='reviews'),
    path('create_services', views.create_services, name='create_services'),
]