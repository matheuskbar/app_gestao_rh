from django.urls import path
from .views import ListarFuncionarios

app_name = 'funcionarios'
urlpatterns = [
    path('', ListarFuncionarios.as_view(), name='listar_funcionarios')
]
