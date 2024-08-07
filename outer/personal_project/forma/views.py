from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'sights/index.html')


def formauser(request):
    if request.method == "GET":
        return render(request, 'forma/formauser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('registerform')
            except IntegrityError:
                return render(request, 'forma/formauser.html',
                              {'form': UserCreationForm(),
                               'error':
                                   'Такое имя пользователя уже существует. Задайте другое'})

        else:
            return render(request, 'forma/formauser.html', {'form': UserCreationForm(),
                                                            'error': 'Пароли не совпадают'})


def registerform(request):
    return render(request, 'forma/registerform.html')


def home(request):
    return render(request, 'forma/home.html')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == "GET":
        return render(request, 'forma/loginuser.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'forma/loginuser.html',
                          {'form': AuthenticationForm(),
                           'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('registerform')


@login_required
def personaluser(request):
    return render(request, 'forma/personaluser.html')


@login_required
def guideuser(request):
    return render(request, 'forma/guideuser.html')