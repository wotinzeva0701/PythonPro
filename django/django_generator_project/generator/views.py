from django.shortcuts import render
from django.http import HttpResponse


def rew(request):
    return render(request, "generator/rew.html", {'password': 'hello', 'title':
                                                  "Главная страница"})
