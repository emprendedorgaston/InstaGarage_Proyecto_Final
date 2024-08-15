from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion
from .forms import PublicacionForm
from django.contrib.auth.decorators import login_required

@login_required
def crear_publicacion(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.nombre_autor = request.user.first_name  # Guardar el nombre
            publicacion.apellido_autor = request.user.last_name  # Guardar el apellido
            publicacion.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = PublicacionForm()
    return render(request, 'mensajes/crear_publicacion.html', {'form': form})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'mensajes/detalle_publicacion.html', {'publicacion': publicacion})

def listar_publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    return render(request, 'mensajes/listar_publicaciones.html', {'publicaciones': publicaciones})

@login_required
def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk, autor=request.user)
    if request.method == "POST":
        form = PublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = PublicacionForm(instance=publicacion)
    return render(request, 'mensajes/editar_publicacion.html', {'form': form})
