from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('geeksforgeeks/', views.geeksforgeeks),
    path('earthlydev/', views.earthlydev),
]
