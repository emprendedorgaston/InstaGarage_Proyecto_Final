from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion_corta = models.CharField(max_length=300)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='publicaciones/')
    url = models.URLField(max_length=200, blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_publicaciones')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
from django.db import models
from django.contrib.auth.models import User
from mensajes.models import Publicacion

class Comentario(models.Model):
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name="comentarios")

    def __str__(self):
        return f"{self.autor} - {self.publicacion}"


class Instagarage(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='instagarages/')

    def __str__(self):
        return self.titulo
