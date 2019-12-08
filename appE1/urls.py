from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('articulos/', views.articulos, name='articulos'),
    path('articulo/<int:articulo_id>/', views.articulo, name='articulo'),
    path('redactores/', views.redactores, name='redactores'),
    path('redactor/<int:redactor_id>/', views.redactor, name='redactor'),
    path('contacto/', views.contacto, name='contacto')
]