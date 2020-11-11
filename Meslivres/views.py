# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'Meslivres/index.html')
