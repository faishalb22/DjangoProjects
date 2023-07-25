from django.conf.urls import url
from appTwo import views

urlpatterns = [
    path('users/', views.users),
]