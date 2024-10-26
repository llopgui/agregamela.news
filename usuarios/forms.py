"""
Forms for the usuarios app.

This module contains all the forms needed for user management:
- Registration
- Profile update
- User update
"""

from typing import Any, Dict
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import Perfil

User = get_user_model()

class UsuarioRegistroForm(UserCreationForm):
    """
    Form for user registration.
    
    Extends Django's UserCreationForm to include email field.
    """
    
    email = forms.EmailField(
        required=True,
        help_text=_('Requerido. Ingrese una dirección de email válida.')
    )
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
    
    def clean_email(self) -> str:
        """
        Validate that the email is unique.
        
        Returns:
            str: The validated email
            
        Raises:
            ValidationError: If email is already in use
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                _('Ya existe un usuario con este email.')
            )
        return email

class UsuarioUpdateForm(forms.ModelForm):
    """
    Form for updating user information.
    """
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the form with custom field attributes.
        """
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

class PerfilUpdateForm(forms.ModelForm):
    """
    Form for updating user profile information.
    """
    
    class Meta:
        model = Perfil
        fields = ['imagen', 'bio', 'sitio_web']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

