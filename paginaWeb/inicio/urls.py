from django.urls import path
from .views import inicio, contacto,galery

urlpatterns = [
    path('', inicio, name='inicio'),
    path('contacto/', contacto, name='contacto'),
    path('galery/', galery, name='galery'),
]