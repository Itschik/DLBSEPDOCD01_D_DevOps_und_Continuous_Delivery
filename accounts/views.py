from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/login.html', {'error': 'Ungültige Anmeldedaten'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        if not username or not password:
            return render(request, 'accounts/register.html', {'error': 'Bitte Benutzername/Passwort ausfüllen.'})
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Benutzername existiert bereits.'})
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/register.html')
