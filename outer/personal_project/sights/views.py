from django.shortcuts import render
from .models import Sights


def index(request):
    counts = Sights.objects.all()
    return render(request, 'sights/index.html', {'counts': counts})
