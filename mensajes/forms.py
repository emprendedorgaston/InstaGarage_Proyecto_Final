from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'descripcion_corta', 'descripcion', 'precio', 'imagen', 'url']  # Incluye el campo URL
