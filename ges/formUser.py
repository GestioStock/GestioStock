from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

RANGO_USER = [("ADMIN", "admin"), ("BODEGUERO", "bodeguero")]

class CustomUserCreationForm(UserCreationForm):
    nombre = forms.CharField(max_length=25, min_length=2, required=True) 
    apellido = forms.CharField(max_length=25, min_length=2, required=True)
    rut = forms.CharField(max_length=12, min_length=10, required=True)
    rango = forms.ChoiceField(label='Rando de Usuario', choices = RANGO_USER)
    
    class Meta:
        model = User
        fields = ['username', "nombre", "apellido", "rut", "rango", "password1", "password2"]