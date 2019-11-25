from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articulo/<int:articulo_id>/', views.detail, name='articulo')
]