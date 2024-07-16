from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_rotativo/', views.cadastrar_rotativo, name='cadastrar_rotativo'),
    path('listar_rotativo/', views.listar_rotativo, name='listar_rotativo'),
    path('deletar_rotativo/<int:id>', views.deletar_rotativo, name='deletar_rotativo'),
    path('exibir_rotativo/<int:id>', views.exibir_rotativo, name='exibir_rotativo'),
    path('editar_rotativo/<int:id>', views.editar_rotativo, name='editar_rotativo'),
]