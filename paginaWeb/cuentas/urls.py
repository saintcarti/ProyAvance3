from django.urls import path

from .views import  exit
urlpatterns = [
    path('logout/', exit, name='logout'),
]
