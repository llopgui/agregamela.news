from typing import List
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Perfil.
    
    Attributes:
        list_display: Campos que se mostrarán en la lista de perfiles
        list_filter: Campos por los que se podrá filtrar
        search_fields: Campos por los que se podrá buscar
        ordering: Orden por defecto de los registros
    """
    
    list_display: List[str] = [
        'usuario', 'email', 'nickname', 'bio', 'facebook', 'twitter', 'instagram',
        'imagen', 'premium', 'karma', 'votos_positivos', 'votos_negativos', 
        'posts', 'comentarios', 'guardados', 'estado', 'fecha_registro'
    ]
    list_filter: List[str] = ['fecha_registro', 'estado', 'premium']
    search_fields: List[str] = ['usuario__username', 'bio', 'email', 'nickname']
    ordering: List[str] = ['-fecha_registro']
    
    readonly_fields: List[str] = ['fecha_registro']
    
    fieldsets = (
        (_('Información de Usuario'), {
            'fields': ('usuario', 'email', 'nickname', 'bio', 'facebook', 'twitter', 'instagram', 'imagen')
        }),
        (_('Información de Estado'), {
            'fields': ('estado', 'premium', 'karma', 'votos_positivos', 'votos_negativos', 'posts', 'comentarios', 'guardados')
        }),
        (_('Información Temporal'), {
            'fields': ('fecha_registro',),
            'classes': ('collapse',)
        }),
    )
