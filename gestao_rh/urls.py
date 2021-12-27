from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('empresas/', include('empresas.urls')),
]
