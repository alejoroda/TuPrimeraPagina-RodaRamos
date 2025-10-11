from django import forms
from .models import Producto
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class PostForm(forms.ModelForm):    
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria', 'imagen'] 

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fecha_nacimiento = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Fecha de nacimiento"
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "fecha_nacimiento"]

    def save(self, commit=True):
        user = super().save(commit)
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        if commit:
            perfil, created = Perfil.objects.get_or_create(user=user)
            perfil.fecha_nacimiento = fecha_nacimiento
            perfil.save()
        return user

# Formulario para comentarios
from .models import Comentario
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'placeholder': 'Escribe tu comentario...'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['fecha_nacimiento', 'imagen']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
