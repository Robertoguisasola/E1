from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Redactor, Articulo

admin.site.register(Redactor)
admin.site.register(Articulo)
