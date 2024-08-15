# principal/views.py
from django.shortcuts import render, get_object_or_404
from mensajes.models import Publicacion  # Usamos el modelo de mensajes

def home(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    return render(request, 'principal/base.html', {'publicaciones': publicaciones})

def acerca_de(request):
    return render(request, 'principal/acerca_de.html')

def listar_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'principal/listar_publicaciones.html', {'publicaciones': publicaciones})
# principal/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion, Comentario
from .forms import PublicacionForm, ComentarioForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from .models import Publicacion

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'principal/detalle_publicacion.html', {'publicacion': publicacion})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from mensajes.models import Publicacion

@login_required
def perfil(request):
    publicaciones = Publicacion.objects.filter(autor=request.user)
    return render(request, 'principal/perfil.html', {'publicaciones': publicaciones})

@login_required
def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk, autor=request.user)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('perfil')
    return render(request, 'principal/eliminar_publicacion.html', {'publicacion': publicacion})
