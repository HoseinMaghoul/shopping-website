from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'Username or Password is wrong','danger')
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['full_name'], cd['password'])
            user.save()
            messages.success(request, 'You are registered successfully', 'success')
            return redirect('shop:home')
    else:
        form = UserRegisterationForm()
    return render(request, 'accounts/register.html', {'form':form})


def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('accounts:login')
