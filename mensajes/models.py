from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion_corta = models.CharField(max_length=300)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='publicaciones/')
    url = models.URLField(max_length=200, blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_autor = models.CharField(max_length=50, null=True, blank=True)
    apellido_autor = models.CharField(max_length=50, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

from django.db import models
from django.contrib.auth.models import User
from principal.models import Publicacion

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios_mensajes')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios_mensajes')
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.username} - {self.publicacion.titulo}"
