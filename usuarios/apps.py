from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    """Configuración de la aplicación Usuarios."""

    default_auto_field = "django.db.models.BigAutoField"
    # Cambia el name para reflejar la ruta completa del módulo
    name = "usuarios"

    def ready(self) -> None:
        """Importa las señales cuando la aplicación está lista."""
        # Importación relativa en lugar de absoluta
        import usuarios.signals

