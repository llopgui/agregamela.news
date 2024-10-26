from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Perfil

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs) -> None:
    """
    Crea un Perfil automáticamente cuando se crea un nuevo usuario.
    """
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs) -> None:
    """
    Guarda el Perfil del usuario cuando se actualiza el usuario.
    """
    instance.perfil.save()
