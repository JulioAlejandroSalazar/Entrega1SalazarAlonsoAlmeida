from django.shortcuts import render
from .models import *
from .forms import *

def inicio(request):
    return render(request, "inicio.html")



def autores(request):
    formulario = Autor_Form()
    if request.method == "POST":
        form = Autor_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre= info["nombre"]
            apellido = info["apellido"]
            email = info["email"]
            fecha_nacimiento = info["fecha_nacimiento"]
            autor = Autor(nombre = nombre, apellido = apellido, email = email, fecha_nacimiento = fecha_nacimiento)
            autor.save()
            return render(request, "autores.html", {"formulario" : formulario, "mensaje" : "autor creado exitosamente"})

    return render(request, "autores.html", {"formulario" : formulario})


def busqueda_autores(request):
    return render(request, "Busqueda/busqueda_autores.html")


def autores_buscado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        autores = Autor.objects.filter(nombre = nombre)
        return render(request, "Busqueda/autores_buscado.html", {"autores" : autores})

    return render(request, "Busqueda/busqueda_autores.html", {"mensaje" : "Ingrese un autor"})



def publicaciones(request):
    formulario = Publicacion_Form()
    if request.method == "POST":
        form = Publicacion_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            titulo = info["titulo"]
            descripcion = info["descripcion"]
            contenido = info["contenido"]
            fecha = info["fecha"]
            publicacion = Publicacion(titulo = titulo, descripcion = descripcion, contenido = contenido, fecha = fecha)
            publicacion.save()
            return render(request, "publicaciones.html", {"formulario" : formulario, "mensaje" : "publicacion creada exitosamente"})

    return render(request, "publicaciones.html", {"formulario" : formulario})


def busqueda_publicaciones(request):
    return render(request, "Busqueda/busqueda_publicaciones.html")


def publicaciones_buscado(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        publicacion = Publicacion.objects.filter(titulo = titulo)
        return render(request, "Busqueda/publicaciones_buscado.html", {"publicacion" : publicacion})

    return render(request, "Busqueda/busqueda_publicaciones.html", {"mensaje" : "Ingrese un titulo"})



def autores_miembro(request):
    formulario = Autor_Miembro_Form()
    if request.method == "POST":
        form = Autor_Miembro_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre= info["nombre"]
            apellido = info["apellido"]
            email = info["email"]
            fecha_nacimiento = info["fecha_nacimiento"]
            autor = Autor_Miembro(nombre = nombre, apellido = apellido, email = email, fecha_nacimiento = fecha_nacimiento)
            autor.save()
            return render(request, "autores_miembro.html", {"formulario" : formulario, "mensaje" : "autor creado exitosamente"})

    return render(request, "autores_miembro.html", {"formulario" : formulario})


def busqueda_autores_miembro(request):
    return render(request, "Busqueda/busqueda_autores_miembro.html")


def autores_miembro_buscado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        autores = Autor_Miembro.objects.filter(nombre = nombre)
        return render(request, "Busqueda/autores_miembro_buscado.html", {"autores" : autores})

    return render(request, "Busqueda/busqueda_autores_miembro.html", {"mensaje" : "Ingrese un nombre"})
