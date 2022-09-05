from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    contenido = models.CharField(max_length= 2000)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.titulo}"


class Autor_Miembro(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    es_miembro = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"