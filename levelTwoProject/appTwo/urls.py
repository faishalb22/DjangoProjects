from django.urls import path
from appTwo import views

urlpatterns = [
    #path('index/', views.index),
    path('users/', views.users),
]