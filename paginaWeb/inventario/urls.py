from django.urls import path
from . import views

urlpatterns = [
    path('mercado/', views.inventario_view, name='inventario'),
    path('API/', views.API, name='API'),
    path('inventario_stock/',views.listado_camaras, name='listado_camaras'),
    path('inventario_stock/detalle_camara/<int:id>/',views.detalle_camara, name= 'detalle_camara'),
    path('inventario_stock/crear_camara/',views.crear_camara, name= 'crear_camara'),
    path('inventario_stock/editar_camara/<int:id>/',views.editar_camara, name= 'editar_camara'),

]
