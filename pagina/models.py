from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True, default="ejemplo@gmail.com")

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = "B" , "Borrador"
        PUBLICADO = "P" , "Publicado"
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechapublicacion = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.CharField(max_length=1,choices=Estado.choices, default=Estado.BORRADOR)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="compras")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre}"