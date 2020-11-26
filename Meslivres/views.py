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
def misàjour(request,):
     return render(request,'Meslivres/misàjour.html')
def ajout(request,):
     return render(request,'Meslivres/ajout.html')
def profile(request,):
     return render(request,'Meslivres/profile.html')
def comp_profil(request,):
     return render(request,'Meslivres/comp_profil.html')

def get_utilisateur(request):
       form = forms.utilisateurForm()
       if request.method == 'POST':
            form = forms.utilisateurForm(request.POST)
            if form.is_valid():
               form.save()
               return HttpResponse('Success') # or you redirect anywhere you want to