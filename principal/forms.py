# principal/forms.py

from django import forms
from .models import Publicacion, Comentario

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'descripcion', 'precio', 'modelo', 'imagen']

class ComentarioForm(forms.ModelForm):
    texto = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 3,
        'placeholder': 'Escribe tu comentario aquí...'
    }))

    class Meta:
        model = Comentario
        fields = ['texto']
