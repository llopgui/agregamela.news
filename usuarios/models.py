from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from typing import Any

# Modelo de perfil de usuario
class Perfil(models.Model):
    """
    Modelo que representa el perfil de un usuario.
    """

    id: models.UUIDField = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        help_text="Identificador único del perfil."
    )
    usuario: models.OneToOneField = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil',
        help_text="Usuario asociado al perfil."
    )
    email: models.EmailField = models.EmailField(
        unique=True,
        help_text="Correo electrónico único del usuario."
    )
    fecha_registro: models.DateTimeField = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de registro del perfil."
    )
    nickname: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        help_text="Apodo del usuario."
    )
    bio: models.TextField = models.TextField(
        max_length=500,
        blank=True,
        help_text="Biografía del usuario."
    )
    facebook: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        help_text="URL de Facebook del usuario."
    )
    twitter: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        help_text="URL de Twitter del usuario."
    )
    instagram: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        help_text="URL de Instagram del usuario."
    )
    imagen: models.ImageField = models.ImageField(
        upload_to='usuarios/img/perfiles/',
        default='usuarios/img/perfiles/default/imagen_de_perfil_predeterminada.png',
        help_text="Imagen de perfil del usuario."
    )
    lista_negra: models.ManyToManyField = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='lista_negra_de',
        help_text="Lista negra de usuarios."
    )
    suscripciones: models.ManyToManyField = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='suscriptores',
        help_text="Usuarios a los que está suscrito."
    )
    premium: models.BooleanField = models.BooleanField(
        default=False,
        help_text="Indica si el usuario tiene una cuenta premium."
    )
    karma: models.IntegerField = models.IntegerField(
        default=0,
        help_text="Puntuación de karma del usuario."
    )
    votos_positivos: models.IntegerField = models.IntegerField(
        default=0,
        help_text="Cantidad de votos positivos recibidos."
    )
    votos_negativos: models.IntegerField = models.IntegerField(
        default=0,
        help_text="Cantidad de votos negativos recibidos."
    )
    posts: models.IntegerField = models.IntegerField(
        default=0,
        help_text="Cantidad de publicaciones realizadas."
    )
    comentarios: models.IntegerField = models.IntegerField(
        default=0,
        help_text="Cantidad de comentarios realizados."
    )
    guardados: models.IntegerField = models.IntegerField(
        default=0,
        help_text="Cantidad de elementos guardados."
    )
    estado: models.CharField = models.CharField(
        max_length=100,
        default='activo',
        choices=[
            ('activo', 'Activo'),
            ('inactivo', 'Inactivo'),
            ('bloqueado', 'Bloqueado'),
            ('suspendido', 'Suspendido'),
            ('en_revision', 'En revisión'),
            ('baneado', 'Baneado'),
            ('eliminado', 'Eliminado'),
        ],
        help_text="Estado actual del perfil."
    )
    verificado: models.BooleanField = models.BooleanField(
        default=False,
        help_text="Indica si el perfil ha sido verificado."
    )
    sitio_web: models.URLField = models.URLField(
        max_length=200,
        blank=True,
        help_text="Sitio web personal del usuario."
    )
    localidad: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        help_text="Localidad del usuario."
    )
    pais: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        help_text="País del usuario."
    )
    fecha_nacimiento: models.DateField = models.DateField(
        blank=True,
        null=True,
        help_text="Fecha de nacimiento del usuario."
    )
    genero: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        choices=[
            ('masculino', 'Masculino'),
            ('femenino', 'Femenino'),
        ],
        help_text="Género del usuario."
    )
    class Meta:
        """Configuración del modelo."""
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-fecha_registro']
        indexes = [
            models.Index(fields=['usuario']),
            models.Index(fields=['email']),
            models.Index(fields=['nickname']),
            models.Index(fields=['estado']),
        ]

    def __str__(self) -> str:
        """Retorna una representación en cadena del perfil."""
        return f'Perfil de {self.usuario.username}'

    def get_karma_total(self) -> int:
        """
        Calcula y retorna el karma total del usuario.
        
        Returns:
            int: Karma total calculado
        """
        return self.votos_positivos - self.votos_negativos

    def actualizar_karma(self) -> None:
        """Actualiza el karma basado en votos positivos y negativos."""
        self.karma = self.get_karma_total()
        self.save(update_fields=['karma'])

    def get_estado_display(self) -> str:
        """
        Retorna el estado formateado para mostrar.
        
        Returns:
            str: Estado formateado
        """
        return dict(self._meta.get_field('estado').choices)[self.estado]

    def toggle_premium(self) -> None:
        """Alterna el estado premium del usuario."""
        self.premium = not self.premium
        self.save(update_fields=['premium'])

    def agregar_a_lista_negra(self, usuario: 'Perfil') -> None:
        """
        Agrega un usuario a la lista negra.
        
        Args:
            usuario: Perfil del usuario a agregar
        """
        if usuario != self:
            self.lista_negra.add(usuario)

    def quitar_de_lista_negra(self, usuario: 'Perfil') -> None:
        """
        Quita un usuario de la lista negra.
        
        Args:
            usuario: Perfil del usuario a quitar
        """
        self.lista_negra.remove(usuario)

    def toggle_suscripcion(self, usuario: 'Perfil') -> bool:
        """
        Alterna la suscripción a un usuario.
        
        Args:
            usuario: Perfil del usuario para alternar suscripción
            
        Returns:
            bool: True si se suscribió, False si se desuscribió
        """
        if usuario in self.suscripciones.all():
            self.suscripciones.remove(usuario)
            return False
        else:
            self.suscripciones.add(usuario)
            return True

    def clean(self) -> None:
        """
        Valida los datos del modelo antes de guardar.
        
        Raises:
            ValidationError: Si hay errores en los datos
        """
        super().clean()
        from django.core.validators import URLValidator
        validator = URLValidator()
        if self.facebook:
            validator(self.facebook)
        if self.twitter:
            validator(self.twitter)
        if self.instagram:
            validator(self.instagram)

    def save(self, *args: Any, **kwargs: Any) -> None:
        """
        Guarda el perfil con validaciones adicionales.
        
        Args:
            *args: Argumentos posicionales
            **kwargs: Argumentos nombrados
        """
        if self.pk:  # Solo si el objeto ya existe
            self.karma = self.get_karma_total()
        
        if self.usuario and not self.email:
            self.email = self.usuario.email
            
        super().save(*args, **kwargs)
