from django.urls import path
from .views import inicio, contacto,galery,base

urlpatterns = [
    path('', inicio, name='inicio'),
    path('contacto/', contacto, name='contacto'),
    path('galery/', galery, name='galery'),
    path('base/', base, name='base'),
]