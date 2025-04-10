from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'sbc_app/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'sbc_app/login.html')


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')