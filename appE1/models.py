from django.db import models

# Create your models here.
class Redactor(models.Model):
    nombre = models.CharField(max_length=99, default='')
    apellido = models.CharField(max_length=99, default='')

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    redactor = models.ForeignKey(Redactor, on_delete=models.CASCADE)
    titular = models.CharField(max_length=100, default='')
    entradilla = models.TextField()
    noticia = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.titular
