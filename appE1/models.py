from django.db import models
from datetime import datetime


# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=99, default='')
    apellido = models.CharField(max_length=99, default='')

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titular = models.CharField(max_length=100, default='')
    entradilla = models.TextField()
    noticia = models.TextField()
    fecha = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.titular
