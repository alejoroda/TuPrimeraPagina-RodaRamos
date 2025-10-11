from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True, default="ejemplo@gmail.com")

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    CATEGORIAS_PREDEFINIDAS = [
        ("Comedor", "Comedor"),
        ("Sillones y Sillas", "Sillones y Sillas"),
        ("Decoración de Interior", "Decoración de Interior"),
        ("Baño", "Baño"),
        ("Iluminación", "Iluminación"),
        ("Cortinas", "Cortinas"),
        ("Oficina", "Oficina"),
        ("Otros", "Otros"),
    ]
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_PREDEFINIDAS)

    def __str__(self):
        return self.categoria

class Producto(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = "B" , "Borrador"
        PUBLICADO = "P" , "Publicado"
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
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



class Comentario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    respuesta = models.TextField(blank=True, null=True)  # Respuesta del autor

    def __str__(self):
        return f'Comentario de {self.autor} en {self.producto.nombre}'

class Respuesta(models.Model):
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='respuestas')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'posts.html'

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='perfiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def crear_o_actualizar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    else:
        try:
            instance.perfil.save()
        except Perfil.DoesNotExist:
            Perfil.objects.create(user=instance)

