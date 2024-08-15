from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
    path('publicaciones/', views.listar_publicaciones, name='listar_publicaciones'),
    path('publicacion/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('perfil/', views.perfil, name='perfil'),
    path('eliminar_publicacion/<int:pk>/', views.eliminar_publicacion, name='eliminar_publicacion'),
]
