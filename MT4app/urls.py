from . import views
from django.urls import path

urlpatterns = [
    path('', views.welcome, name='home'),
    path('services', views.services, name='services'),
    path('reviews', views.ReviewCreateView.as_view(), name='reviews'),
    path('create_services', views.create_services, name='create_services'),
    path('edit_service/<int:service_id>/', views.edit_service, name='edit_service'),
    path('delete_service/<int:service_id>/', views.delete_service, name='delete_service'),
]