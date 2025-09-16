from django import forms
from .models import EquipoFutbol
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EquipoFutbolForm(forms.ModelForm):
    class Meta:
        model = EquipoFutbol
        fields = ["nombre", "ciudad", "fundacion", "estadio"]

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

