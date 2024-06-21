from django.db import models
from distutils.command.upload import upload

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name='Id de la categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

class Marca(models.Model):
    idMarca = models.AutoField(primary_key=True, verbose_name='Id de la marca')
    nombreMarca = models.CharField(max_length=50, verbose_name='Nombre de la marca')

    def __str__(self):
        return self.nombreMarca


class Camara(models.Model):
    idCamara = models.AutoField(primary_key=True, verbose_name='Id de la camara')
    nombreCamara = models.CharField(max_length=50, verbose_name='Nombre de la camara')
    precio = models.IntegerField(verbose_name='Precio de la camara')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100, verbose_name='Descripcion de la camara')
    imagen = models.ImageField(upload_to='imagenes',null=True,verbose_name='Imagen de la camara')

    def __str__(self):
        return self.get_codigo_name()
    
    def get_codigo_name(self):
        return f"Camara {self.nombreCamara} - {self.marca.nombreMarca} - {self.categoria.nombreCategoria}"
