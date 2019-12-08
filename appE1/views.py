from django.shortcuts import render, get_list_or_404, get_object_or_404
from appE1.models import Articulo, Redactor


def index(request):
    return render(request, 'index.html')


# Devuelve un listado de artículos
def articulos(request):
    articulos = get_list_or_404(Articulo.objects.order_by('-fecha'))
    context = {'listaArticulos': articulos}
    return render(request, 'articulos.html', context)


# Devuelve los detalles de un artículo
def articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    context = {'articulo': articulo}
    return render(request, 'articulo.html', context)


def redactores(request):
    redactores = get_list_or_404(Redactor.objects.order_by('nombre'))
    context = {'listaRedactores': redactores}
    return render(request, 'redactores.html', context)


def redactor(request, redactor_id):
    redactor = get_object_or_404(Redactor, pk=redactor_id)
    articulos = get_list_or_404(Articulo.objects.order_by('titular'))
    context = {'redactor': redactor, 'listaArticulos': articulos}
    return render(request, 'redactor.html', context)

def contacto(request):
    return render(request, 'contacto.html')