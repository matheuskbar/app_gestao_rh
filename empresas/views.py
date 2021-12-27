from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from empresas.models import Empresa


class NovaEmpresa(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        empresa = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = empresa
        funcionario.save()
        return redirect('core:index')


class EditarEmpresa(UpdateView):
    model = Empresa
    fields = ['nome']
