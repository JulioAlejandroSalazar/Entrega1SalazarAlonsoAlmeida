from django.shortcuts import render
#from .models import *
#from .forms import *

#reemplazar links con nombres adecuados segun los models
def inicio(request):
    return render(request, "inicio.html")


def link1(request):
    if request.method == "POST":
        form = link1Form(request.POST)
        if form.is_valid:
            info = form.cleaned_data
            atributo1 = info["atributo1"]
            atributo2 = info["atributo2"]
            link1model = link1Model(atributo1 = atributo1, atributo2 = atributo2)
            link1model.save()
            return render(request, "link1.html", {"formulario" : formulario, "mensaje" : "link1 creado exitosamente"})

    formulario = link1Form()
    return render(request, "link1.html", {"formulario" : formulario})


def busqueda_link1(request):
    return render(request, "busqueda_link1.html")


def link1_buscado(request):
    if request.GET["atributo"]:
        atributo = request.GET["atributo"]
        link1 = link1Model.objects.filter(atributo = atributo)
        return render(request, "link1_buscado.html", {"link1" : link1})

    return render(request, "busqueda_link1.html", {"mensaje" : "Ingrese un atributo"})


def link2(request):
    if request.method == "POST":
        form = link2Form(request.POST)
        if form.is_valid:
            info = form.cleaned_data
            atributo1 = info["atributo1"]
            atributo2 = info["atributo2"]
            link2model = link2Model(atributo1 = atributo1, atributo2 = atributo2)
            link2model.save()
            return render(request, "link2.html", {"formulario" : formulario, "mensaje" : "link2 creado exitosamente"})

    formulario = link2Form()
    return render(request, "link2.html", {"formulario" : formulario})


def busqueda_link2(request):
    return render(request, "busqueda_link2.html")


def link2_buscado(request):
    if request.GET["atributo"]:
        atributo = request.GET["atributo"]
        link2 = link2Model.objects.filter(atributo = atributo)
        return render(request, "link2_buscado.html", {"link2" : link2})

    return render(request, "busqueda_link2.html", {"mensaje" : "Ingrese un atributo"})


def link3(request):
    if request.method == "POST":
        form = link3Form(request.POST)
        if form.is_valid:
            info = form.cleaned_data
            atributo1 = info["atributo1"]
            atributo2 = info["atributo2"]
            link3model = link3Model(atributo1 = atributo1, atributo2 = atributo2)
            link3model.save()
            return render(request, "link3.html", {"formulario" : formulario, "mensaje" : "link3 creado exitosamente"})

    formulario = link3Form()
    return render(request, "link3.html", {"formulario" : formulario})


def busqueda_link3(request):
    return render(request, "busqueda_link3.html")


def link3_buscado(request):
    if request.GET["atributo"]:
        atributo = request.GET["atributo"]
        link3 = link3Model.objects.filter(atributo = atributo)
        return render(request, "link3_buscado.html", {"link3" : link3})

    return render(request, "busqueda_link3.html", {"mensaje" : "Ingrese un atributo"})
