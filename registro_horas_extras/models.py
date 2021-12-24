from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Registro hora extra'
        verbose_name_plural = 'Registro horas extras'

    def __str__(self):
        return self.motivo
