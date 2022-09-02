from django.urls import path
from .views import *


urlpatterns = [
path('', inicio, name="inicio"),

path('link1/', link1, name="link1"),
path('busqueda_link1/', busqueda_link1, name="busqueda_link1"),
path('link1_buscado/', link1_buscado, name="link1_buscado"),

path('link2/', link2, name="link2"),
path('busqueda_link2/', busqueda_link2, name="busqueda_link2"),
path('link2_buscado/', link2_buscado, name="link2_buscado"),

path('link3/', link3, name="link3"),
path('busqueda_link3/', busqueda_link3, name="busqueda_link3"),
path('link3_buscado/', link3_buscado, name="link3_buscado"),
]