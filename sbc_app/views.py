from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sbc_app.models import EventoSeguridad  # Asegúrate de que EventoSeguridad esté definido

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Credenciales incorrectas."
    return render(request, 'sbc_app/login.html', {'error': error})

@login_required
def dashboard_view(request):
    eventos = EventoSeguridad.objects.all().order_by('-fecha')
    return render(request, 'sbc_app/dashboard.html', {'eventos': eventos})
