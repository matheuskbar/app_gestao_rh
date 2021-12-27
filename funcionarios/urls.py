from django.urls import path
from .views import ListarFuncionarios, EditarFuncionario, DeletarFuncionario

app_name = 'funcionarios'
urlpatterns = [
    path('', ListarFuncionarios.as_view(), name='listar_funcionarios'),
    path('editar/<int:pk>', EditarFuncionario.as_view(), name='editar_funcionario'),
    path('deletar/<int:pk>', DeletarFuncionario.as_view(), name='deletar_funcionario'),
]
