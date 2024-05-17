from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from encrypt.models import EncryptedFile

def home_view(request):
    return render(request, 'index.html') 

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email') 
            user = authenticate(username=username, password=password) 
            if user is not None:
                login(request, user)
                return redirect('dashboard')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form}) 

def login_view(request): 
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def dashboard_view(request):        
    user_files = EncryptedFile.objects.all()
    
    context = {
        'user_files': user_files,
        'first_name': request.user.first_name,
    }

    return render(request, 'dashboard.html', context) 