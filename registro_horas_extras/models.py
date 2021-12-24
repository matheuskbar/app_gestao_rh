from django.db import models

from funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Registro hora extra'
        verbose_name_plural = 'Registro horas extras'

    def __str__(self):
        return self.motivo
