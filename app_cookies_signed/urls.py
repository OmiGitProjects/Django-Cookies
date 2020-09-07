from django.urls import path
from .import views

urlpatterns = [
    path('', views.set_cookies, name='set_cookies'),
    path('get/', views.get_cookies, name='get_cookies'),
]