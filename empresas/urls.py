from django.urls import path
from .views import NovaEmpresa, EditarEmpresa

app_name = 'empresas'

urlpatterns = [
    path('nova/', NovaEmpresa.as_view(), name='nova_empresa'),
    path('editar/<int:pk>', EditarEmpresa.as_view(), name='editar_empresa'),
]
