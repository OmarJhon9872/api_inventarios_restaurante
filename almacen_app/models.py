from turtle import mode
from django.db import models

# Create your models here.

class Almacen(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    email = models.EmailField(max_length=255)
    empleados = models.IntegerField()
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    
class Producto(models.Model):
    descripcion = models.CharField(max_length=255)
    stock = models.IntegerField()
    almacen = models.ForeignKey(
        Almacen, 
        on_delete=models.CASCADE, 
        related_name="almacen_nombre",
        null=True
    )
    codigo = models.TextField()
    
    def __str__(self):
        return self.descripcion