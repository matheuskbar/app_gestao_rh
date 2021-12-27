from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    usuario = request.user
    context = {
        'usuario': usuario
    }
    return render(request, 'core/index.html', context)
