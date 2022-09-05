from django.urls import path
from .views import *


urlpatterns = [
path('', inicio, name="inicio"),

path('autores/', autores, name="autores"),
path('busqueda_autores/', busqueda_autores, name="busqueda_autores"),
path('autores_buscado/', autores_buscado, name="autores_buscado"),

path('publicaciones/', publicaciones, name="publicaciones"),
path('busqueda_publicaciones/', busqueda_publicaciones, name="busqueda_publicaciones"),
path('publicaciones_buscado/', publicaciones_buscado, name="publicaciones_buscado"),

path('autores_miembro/', autores_miembro, name="autores_miembro"),
path('busqueda_autores_miembro/', busqueda_autores_miembro, name="busqueda_autores_miembro"),
path('autores_miembro_buscado/', autores_miembro_buscado, name="autores_miembro_buscado"),
]