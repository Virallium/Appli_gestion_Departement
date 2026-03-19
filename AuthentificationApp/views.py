from django.shortcuts import render, redirect
from .models import Profil
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
def register_view(request):
    if request.method=="POST":
        nom_Utilisateur=request.POST['name']
        postnom=request.POST['postname']
        prenom=request.POST['pren']
        telephone=request.POST['num']
        mail=request.POST['mail']
        Adresse=request.POST['Ad']
        mpass=request.POST['password']
        mon_Utilisateur=User.objects.create_user(username=nom_Utilisateur,email=mail,password=mpass)
        mon_Utilisateur.first_name=prenom
        mon_Utilisateur.last_name=postnom
        mon_Utilisateur.save()
        Profil.objects.create(user=mon_Utilisateur,adresse=Adresse,numero=telephone)
        messages.success(request,'Votre compte a été crée avec succèes')
        return redirect('login')
    return render(request, 'auth/register.html')

def login_view(request):
    if request.method=="POST":
        nom_Utilisateur=request.POST['username']
        mpass=request.POST['password']
        user=authenticate(username=nom_Utilisateur, password=mpass)
        if user is not None:
            login(request,user)
            messages.success(request,'Vous vous ète connecté')
            return redirect('Accueil')
        else:
            messages.error(request,'Nom d\'utilisateur ou mot de passe incorrect')
            return redirect('login')
    return render(request, 'auth/login.html')

def accueil_view(request):
    return render(request, 'pages/index.html')
def Activites(request):
    return render(request,'pages/Activites.html')
def Communaute(request):
    return render(request,'pages/Communaute.html')
def Contact(request):
    
    return render(request,'pages/Contact.html')
def Politiques(request):
    return render(request,'pages/politiques.html')
def aide(request):
    return render(request,'pages/aide.html')
