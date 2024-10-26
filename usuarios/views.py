from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, View
from django.utils.translation import gettext_lazy as _
from typing import Type, Optional, Any, Dict

from .forms import (
    UsuarioRegistroForm,
    UsuarioUpdateForm,
    PerfilUpdateForm
)
from usuarios.models import Perfil

User = get_user_model()

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'usuarios/index.html')   

class RegistroUsuarioView(SuccessMessageMixin, CreateView):
    """
    View for user registration.
    
    Attributes:
        template_name: Template used for rendering the registration form
        form_class: Form class used for user registration
        success_url: URL to redirect after successful registration
        success_message: Message to display after successful registration
    """
    
    template_name: str = 'usuarios/registro.html'
    form_class: Type[UsuarioRegistroForm] = UsuarioRegistroForm
    success_url: str = reverse_lazy('usuarios:login')
    success_message: str = _("¡Registro exitoso! Ya puedes iniciar sesión.")
    
    def form_valid(self, form: UsuarioRegistroForm) -> HttpResponse:
        """
        Handle valid form submission.
        
        Args:
            form: The validated form instance
            
        Returns:
            HttpResponse: Redirect to success URL
        """
        response = super().form_valid(form)
        # Crear perfil automáticamente
        Perfil.objects.create(usuario=self.object)
        return response

class PerfilUsuarioView(LoginRequiredMixin, DetailView):
    """
    View for displaying user profile.
    
    Attributes:
        model: The model to use for this view
        template_name: Template used for rendering the profile
        context_object_name: Name used for the object in template context
    """
    
    model: Type[User] = User
    template_name: str = 'usuarios/perfil.html'
    context_object_name: str = 'usuario'
    
    def get_object(self, queryset: Optional[QuerySet] = None) -> User:
        """
        Return the current logged-in user.
        
        Returns:
            User: The current user instance
        """
        return self.request.user

class EditarPerfilView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    View for editing user profile.
    
    Attributes:
        model: The model to use for this view
        template_name: Template used for rendering the edit form
        success_url: URL to redirect after successful update
        success_message: Message to display after successful update
    """
    
    model = User
    template_name = 'usuarios/editar_perfil.html'
    success_url = reverse_lazy('usuarios:perfil')
    success_message = _("¡Perfil actualizado exitosamente!")
    
    def get_object(self, queryset=None):
        """
        Return the current logged-in user.
        
        Returns:
            User: The current user instance
        """
        return self.request.user
    
    def get_form(self, form_class=None):
        """
        Return the form classes for both user and profile forms.
        
        Returns:
            tuple: Tuple containing both form instances
        """
        user_form = UsuarioUpdateForm(instance=self.request.user)
        profile_form = PerfilUpdateForm(instance=self.request.user.perfil)
        return user_form, profile_form
    
    def get_context_data(self, **kwargs):
        """
        Insert the forms into the context dict.
        
        Returns:
            dict: Context dictionary with both forms
        """
        context = super().get_context_data(**kwargs)
        user_form, profile_form = self.get_form()
        context['user_form'] = user_form
        context['profile_form'] = profile_form
        return context
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        """
        Handle POST request to process both forms.
        
        Args:
            request: The HTTP request object
            *args: Additional positional arguments
            **kwargs: Additional keyword arguments
            
        Returns:
            HttpResponse: Redirect to success URL or render form with errors
        """
        user_form = UsuarioUpdateForm(request.POST, instance=request.user)
        profile_form = PerfilUpdateForm(request.POST, request.FILES, instance=request.user.perfil)
        
        # Verifica si ambos formularios son válidos
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, self.success_message)
            return redirect(self.success_url)
        else:
            # Si hay errores, renderiza de nuevo con los formularios
            return self.render_to_response(self.get_context_data(user_form=user_form, profile_form=profile_form))

class LogoutView(View):
    """
    Vista para cerrar sesión del usuario.
    
    Esta vista maneja el cierre de sesión y redirige al usuario a la página de inicio.
    """
    
    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Maneja la solicitud POST para cerrar sesión.
        
        Args:
            request: La solicitud HTTP que contiene la información del usuario.
        
        Returns:
            HttpResponseRedirect: Redirige a la página de inicio después de cerrar sesión.
        """
        logout(request)
        return HttpResponseRedirect(reverse('usuarios:login'))
