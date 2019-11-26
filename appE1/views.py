from django.shortcuts import render, get_list_or_404, get_object_or_404

from appE1.models import Articulo


def index(request):
    return render(request, 'index.html')


# Devuelve un listado de post
def articulos(request):
    articulos = get_list_or_404(Articulo.objects.order_by('titular'))
    context = {'listaArticulos': articulos}
    return render(request, 'articulos.html', context)


# Devuelve los datos de un post
def detail(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    context = {'articulo': articulo}
    return render(request, 'detail.html', context)
