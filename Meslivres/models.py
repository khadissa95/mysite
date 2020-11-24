import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models

class utilisateur(models.Model):
    Name = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=30, default="")
    password = models.CharField(max_length=30, default="")
    
    def __str__(self):
        return self.Name
    




