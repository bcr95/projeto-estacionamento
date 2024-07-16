from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('login_cliente/', views.login_cliente, name='login_cliente'),
]