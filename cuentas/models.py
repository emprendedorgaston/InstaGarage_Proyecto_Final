from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    ESTADOS = (
        ('normal', 'Normal'),
        ('owner', 'Owner'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    estado = models.CharField(max_length=10, choices=ESTADOS, default='normal')

    def __str__(self):
        return f"{self.user.username} - {self.estado}"

    def save(self, *args, **kwargs):
        # Elimina la imagen anterior si ya existe
        if self.pk:
            perfil_antiguo = Perfil.objects.get(pk=self.pk)
            if perfil_antiguo.avatar and perfil_antiguo.avatar != self.avatar:
                perfil_antiguo.avatar.delete(save=False)

        # Personaliza el nombre del archivo con el nombre de usuario
        self.avatar.name = f"avatars/{self.user.username}.jpg"
        super().save(*args, **kwargs)

# Signal para crear el perfil automáticamente al crear un usuario
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()
