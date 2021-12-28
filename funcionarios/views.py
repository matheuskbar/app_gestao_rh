from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .models import Funcionario


class ListarFuncionarios(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset


class CriarFuncionario(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        nome_usuario = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa


class EditarFuncionario(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class DeletarFuncionario(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionarios:listar_funcionarios')
