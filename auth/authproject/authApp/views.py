from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import *


def registerPage(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = RegisterForm()
    context = {
        'form': form,
        'title': 'Register page',
        'btn': 'Register',
    }

    return render(request, 'pages/baseForm.html',context)


def loginPage(request):

    if request.method == 'POST':
        text = request.POST['username']
        password = request.POST['password']

        
        try:
            by_username = UserModel.objects.get(username =text)

            user = authenticate(request, username = by_username.username, password = password )
            if user:
                login(request, user)
                return redirect('dashboard')
        except UserModel.DoesNotExist:
            by_email = UserModel.objects.get(email = text)

            if by_email:
                user = authenticate(request, username = by_email.username , password = password)

                if user:
                    login(request, user)

                    return redirect('dashboard')

    form = AuthForm()
    context = {
        'form': form,
        'title': 'Login page',
        'btn': 'Login',
    }
    return render(request, 'pages/baseForm.html',context)


def dashboardPage(request):
    return render(request, 'pages/dashboard.html')