from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm, PerfilForm
from .models import Perfil

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirige a la página principal después del login
    else:
        form = AuthenticationForm()
    return render(request, 'cuentas/login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'cuentas/registrar.html', {'form': form})


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PerfilForm(instance=request.user.perfil)
    return render(request, 'cuentas/editar_perfil.html', {'form': form})

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('home')

