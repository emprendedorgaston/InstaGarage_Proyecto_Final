# principal/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Publicacion, Comentario
from .forms import ComentarioForm
from django.core.paginator import Paginator
from mensajes.models import Publicacion 

def home(request):
    orden = request.GET.get('orden', 'fecha')
    
    if orden == 'precio':
        publicaciones = Publicacion.objects.all().order_by('precio')
    elif orden == 'alfabeto':
        publicaciones = Publicacion.objects.all().order_by('titulo')
    else:
        publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    
    paginator = Paginator(publicaciones, 20) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'principal/base.html', {'page_obj': page_obj})

def acerca_de(request):
    return render(request, 'principal/acerca_de.html')

def listar_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'principal/listar_publicaciones.html', {'publicaciones': publicaciones})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Publicacion, Comentario
from .forms import ComentarioForm

@login_required
def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    mensaje = None
    error = None
    
    if request.method == "POST":
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.autor = request.user
            comentario.save()
            mensaje = "Comentario enviado con éxito."
        else:
            error = "No se pudo enviar el comentario. Por favor, inténtalo de nuevo."
    else:
        comentario_form = ComentarioForm()

    return render(request, 'principal/detalle_publicacion.html', {
        'publicacion': publicacion,
        'comentario_form': comentario_form,
        'comentarios': publicacion.comentarios.all(),
        'mensaje': mensaje,
        'error': error,
    })


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Publicacion, Comentario

@login_required
def eliminar_comentario(request, publicacion_pk, comentario_pk):
    comentario = get_object_or_404(Comentario, pk=comentario_pk, publicacion_id=publicacion_pk)
    
    # Solo permitir que el dueño del comentario, dueño de la publicación o el owner eliminen el comentario
    if request.user == comentario.autor or request.user == comentario.publicacion.autor or request.user.perfil.estado == 'owner':
        comentario.delete()
        mensaje = "Comentario eliminado con éxito."
    else:
        mensaje = "No tienes permiso para eliminar este comentario."
    
    return redirect('detalle_publicacion', pk=publicacion_pk)

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

def is_owner(user):
    return user.is_authenticated and user.perfil.estado == 'owner'

@login_required
@user_passes_test(is_owner)
def gestionar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'principal/gestionar_usuarios.html', {'usuarios': usuarios})

@login_required
@user_passes_test(is_owner)
def eliminar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    usuario.delete()
    return redirect('gestionar_usuarios')

@login_required
@user_passes_test(is_owner)
def ver_publicaciones_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    publicaciones = Publicacion.objects.filter(autor=usuario)
    return render(request, 'principal/ver_publicaciones_usuario.html', {'usuario': usuario, 'publicaciones': publicaciones})
