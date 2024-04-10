from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from login.forms import CustomUserCreationForm

User = get_user_model()


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('home')  # Redirect to home
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


# def login(request):
#     pass

def logout_confirmation(request):
    return render(request, 'confirm.html')
