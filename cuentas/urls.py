from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('logout/', views.logout_view, name='logout'),  # Ruta para cerrar sesión
]
