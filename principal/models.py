from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    modelo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='publicaciones/')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicaciones_principal')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='publicacion_likes', blank=True)

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.titulo


class Instagarage(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='instagarages/')

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comentario_likes', blank=True)

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'Comentario de {self.autor.username} en {self.publicacion.titulo}'
