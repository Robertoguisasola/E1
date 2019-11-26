from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articulos/', views.articulos, name='articulos'),
    path('articulo/<int:articulo_id>/', views.detail, name='articulo')
]