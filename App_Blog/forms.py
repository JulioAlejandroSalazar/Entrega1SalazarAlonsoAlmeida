from django import forms

class Autor_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()


class Publicacion_Form(forms.Form):
    titulo = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=100)
    contenido = forms.CharField(max_length=2000)
    fecha = forms.DateField()


class Autor_Miembro_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()
    es_miembro = forms.BooleanField()