# Create your views here.
from django.shortcuts import render
from . import forms
from . import models
from django.http import HttpResponse

def index(request,):
     return render(request,'Meslivres/index.html')
def nouveauté(request,):
     return render(request,'Meslivres/nouveauté.html')
def inscript(request,):
     return render(request,'Meslivres/inscript.html')
def populaire(request,):
     return render(request,'Meslivres/populaire.html')

def get_utilisateur(request):
       form = forms.utilisateurForm()
       if request.method == 'POST':
            form = forms.utilisateurForm(request.POST)
            if form.is_valid():
               form.save()
               return HttpResponse('Success') # or you redirect anywhere you want to