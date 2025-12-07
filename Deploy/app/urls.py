from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('check_weather/', views.check_weather, name='check_weather'),  # Add this line
]
