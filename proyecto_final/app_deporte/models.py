from django.db import models

# Create your models here.
class Deporte(models.Model):

    nombre = models.CharField(max_length=40)
    grupo = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nombre_deporte = models.CharField(max_length=30)

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)