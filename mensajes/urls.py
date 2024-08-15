from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_publicacion, name='crear_publicacion'),
    path('publicacion/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('publicacion/<int:pk>/editar/', views.editar_publicacion, name='editar_publicacion'),  # Nueva URL para editar
    path('', views.listar_publicaciones, name='listar_publicaciones'),
]
