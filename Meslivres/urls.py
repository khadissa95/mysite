from django.urls import path

from . import views

urlpatterns = [
    path('/index', views.index, name='index'),
    path('/inscript', views.inscript, name='inscript'),
    path('/nouveauté', views.nouveauté, name='nouveauté'),
    path('/misàjour', views.misàjour, name='misàjour'),
    path('/ajout', views.ajout, name='ajout'),
    path('/comp_profil', views.comp_profil, name='comp_profil'),
    path('/profil', views.profil, name='profil'),
    path('/populaire', views.populaire, name='populaire'),
    
    #path('/', views.get_question, name="utilisateur"),
]