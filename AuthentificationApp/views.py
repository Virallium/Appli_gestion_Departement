from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, ProfilForm, UserLoginForm
from .models import Profil
from django.contrib.auth.decorators import login_required
# 1. INSCRIPTION
def register_view(request):
    if request.method == "POST":
        u_form = UserRegistrationForm(request.POST)
        p_form = ProfilForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            user.set_password(u_form.cleaned_data['password'])
            user.save()
            
            profil = p_form.save(commit=False)
            profil.user = user
            profil.save()
            
            messages.success(request, 'Compte créé ! Vous pouvez vous connecter.')
            return redirect('login')
    else:
        u_form = UserRegistrationForm()
        p_form = ProfilForm()
    return render(request, 'auth/register.html', {'u_form': u_form, 'p_form': p_form})

# 2. CONNEXION
def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user) # Crée la session
                messages.success(request, f'Ravi de vous revoir, {username} !')
                return redirect('Accueil')
            else:
                messages.error(request, 'Identifiants invalides.')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {'form': form})

# 3. DÉCONNEXION
def logout_view(request):
    if request.method=="POST":
        logout(request)
        messages.info(request, 'Vous avez été déconnecté.')
        return redirect('login')
    else:
        return redirect('Accueil')

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
@login_required
def profil_view(request):
    try:
        # On essaie de récupérer le profil
        mon_profil = Profil.objects.get(user=request.user)
    except Profil.DoesNotExist:
        # Si le profil n'existe pas (cas du superuser ou vieux compte)
        # On peut soit créer un profil vide, soit rediriger, soit afficher un message
        messages.warning(request, "Votre profil n'est pas encore complet.")
        return redirect('Accueil') # Ou une autre page de ton choix

    return render(request, 'pages/profil.html', {'profil': mon_profil})