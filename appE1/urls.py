from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('articulos/', views.articulos, name='articulos'),
    path('articulo/<int:articulo_id>/', views.articulo, name='articulo'),
    path('autores/', views.autores, name='autores'),
    path('autor/<int:autor_id>/', views.autor, name='autor')

]