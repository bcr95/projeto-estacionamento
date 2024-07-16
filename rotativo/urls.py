from django.contrib import admin
from django.urls import path, include
from .views import reservar, salvar, listar, editar, update, excluir

urlpatterns = [
    path('reservar/', reservar, name='reservar'),
    path('salvar/', salvar, name='salvar'),
    path('listar/', listar, name='listar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('excluir/<int:id>', excluir, name='excluir'),
]
