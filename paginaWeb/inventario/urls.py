from django.urls import path
from .views import inventario_view, API,listado_camaras

urlpatterns = [
    path('mercado/', inventario_view, name='inventario'),
    path('API/', API, name='API'),
    path('listado_camaras/',listado_camaras, name='listado_camaras'),
]
