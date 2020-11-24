from django import forms
from django.forms import ModelForm
from . import models

class utilisateurForm(ModelForm):
    class Meta:
           model = models.utilisateur
           fields = ['Name', 'email', 'password']
    
