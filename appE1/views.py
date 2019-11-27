from django.shortcuts import render, get_list_or_404, get_object_or_404
from appE1.models import Articulo, Autor


def index(request):
    return render(request, 'index.html')


# Devuelve un listado de artículos
def articulos(request):
    articulos = get_list_or_404(Articulo.objects.order_by('titular'))
    context = {'listaArticulos': articulos}
    return render(request, 'articulos.html', context)


# Devuelve los detalles de un artículo
def articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    context = {'articulo': articulo}
    return render(request, 'articulo.html', context)


def autores(request):
    autores = get_list_or_404(Autor.objects.order_by('nombre'))
    context = {'listaAutores': autores}
    return render(request, 'autores.html', context)


def autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    autor = {'autor': autor}
    return render(request, 'autor.html', context)

