from django.shortcuts import render, get_list_or_404, get_object_or_404

from appE1.models import Articulo


# Devuelve un listado de post
def index(request):
    articulos = get_list_or_404(Articulo.objects.order_by('titular'))
    context = {'listaArticulos': articulos}
    return render(request, 'index.html', context)


def detail(request, articulo_id):
    departamento = get_object_or_404(Articulo, pk=articulo_id)
    context = {'departamento': departamento}
    return render(request, 'detail.html', context)
