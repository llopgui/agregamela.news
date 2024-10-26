from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios import views
from django.conf import settings
from django.conf.urls.static import static


# Namespace para las URLs de usuarios
app_name: str = 'usuarios'

urlpatterns: list = [
    
    # Rutas de autenticación
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='usuarios/login.html'),
        name='login'
    ),
    
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            next_page='usuarios:login'
        ),
        name='logout'
    ),

    # Registro de usuarios
    path(
        'registro/',
        views.RegistroUsuarioView.as_view(),
        name='registro'
    ),

    # Gestión de perfil
    path(
        'perfil/',
        views.PerfilUsuarioView.as_view(),
        name='perfil'
    ),
    
    path(
        'perfil/editar/',
        views.EditarPerfilView.as_view(),
        name='editar_perfil'
    ),
    
    # Gestión de contraseña
    path(
        'password/cambiar/',
        auth_views.PasswordChangeView.as_view(
            template_name='usuarios/password_change.html',
            success_url='usuarios:password_change_done'
        ),
        name='password_change'
    ),

    path(
        'password/cambiar/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='usuarios/password_change_done.html'
        ),
        name='password_change_done'
    ),

    # Recuperación de contraseña
    path(
        'password/reset/',
        auth_views.PasswordResetView.as_view(
            template_name='usuarios/password_reset.html',
            email_template_name='usuarios/password_reset_email.html',
            success_url='usuarios:password_reset_done'
        ),
        name='password_reset'
    ),
    
    path(
        'password/reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='usuarios/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    
    path(
        'password/reset/confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='usuarios/password_reset_confirm.html',
            success_url='usuarios:password_reset_complete'
        ),
        name='password_reset_confirm'
    ),
    
    path(
        'password/reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='usuarios/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]

# Servir archivos de medios durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
