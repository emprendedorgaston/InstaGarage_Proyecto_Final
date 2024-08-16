from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
    path('publicaciones/', views.listar_publicaciones, name='listar_publicaciones'),
    path('publicacion/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('perfil/', views.perfil, name='perfil'),
    path('eliminar_publicacion/<int:pk>/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('gestionar_usuarios/', views.gestionar_usuarios, name='gestionar_usuarios'),
    path('eliminar_usuario/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('ver_publicaciones_usuario/<int:user_id>/', views.ver_publicaciones_usuario, name='ver_publicaciones_usuario'),
    path('publicacion/<int:publicacion_pk>/comentario/<int:comentario_pk>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
]