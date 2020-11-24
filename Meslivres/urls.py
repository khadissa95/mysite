from django.urls import path

from . import views

urlpatterns = [
    path('/index', views.index, name='index'),
    path('/inscript', views.inscript, name='inscript'),
    path('/nouveauté', views.nouveauté, name='nouveauté'),
    path('/populaire', views.populaire, name='populaire'),
    #path('/', views.get_question, name="utilisateur"),
]