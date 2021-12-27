from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from .models import Funcionario


class ListarFuncionarios(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset


class EditarFuncionario(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class DeletarFuncionario(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionarios:listar_funcionarios')
