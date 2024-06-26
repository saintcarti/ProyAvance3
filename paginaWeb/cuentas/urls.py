from django.urls import path

from .views import  exit,iniciosesion
urlpatterns = [
    path('logout/', exit, name='logout'),
    path('login/', iniciosesion, name='login'),
]
