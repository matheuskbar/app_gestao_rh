from django.views.generic import ListView

from .models import Funcionario


class ListarFuncionarios(ListView):
    model = Funcionario
