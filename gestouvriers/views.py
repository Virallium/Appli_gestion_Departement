from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Activites, Membres, versets, Messages
from .form import CustomMembers, CustomActivities, CustomVersets, loginAdmin,ChangePassword
import folium

def activite(request):
    activite_list=Activites.objects.all()
    return render(request, 'pages/voirplus.html',{'activites':activite_list})

def membre(request):
    membre_list=Membres.objects.all()
    verset=versets.objects.all()
    map_obj = folium.Map(location=[-4.4419, 15.2663], zoom_start=10)
    folium.Marker([-4.4419, 15.2663], popup="Kinshasa").add_to(map_obj)
    map_html = map_obj._repr_html_()
    return render(request,'pages/communaute.html',{
        'membres':membre_list,
        'versets':verset,
        'map_html': map_html
    })

def admin(request):
    activites=Activites.objects.all()
    membres=Membres.objects.all()
    verset_bibl=versets.objects.all()
    return render(request,'admin/pages/admin.html',{
        'Activites':activites,
        'Membres':membres,
        'Versets':verset_bibl
    })
#loginAdmin
def connexionadmin(request):
    if request.method == "POST":
        form = loginAdmin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Connexion réussie !')
                return redirect('Admin')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = loginAdmin()
    return render(request,'admin/auth/connection.html',{
        'form': form
    })

def changempass(request):
    # 1. On récupère l'instance de l'utilisateur (User) lié à l'Admin connecté
    # On suppose que l'utilisateur est connecté
    user_instance = request.user 

    if request.method == "POST":
        # 2. On lie le formulaire à l'instance de l'utilisateur
        form = ChangePassword(request.POST, instance=user_instance)
        
        if form.is_valid():
            # 3. Sécurité : On ne sauvegarde pas direct pour hacher le mot de passe
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password) # Hachage du mot de passe
            user.save()
            
            messages.success(request, 'Le mot de passe a été modifié avec succès !')
            return redirect('loginAdmin')
    else:
        # Affichage initial du formulaire vide ou lié à l'instance
        form = ChangePassword(instance=user_instance)
    return render(request, 'admin/auth/changempass.html', {'form': form})

def admin_membres(request):
    if request.method=="POST":
        form=CustomMembers(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Membre ajouté avec succès !')
            return redirect('admin_membres')
    else:
        form=CustomMembers()
def admin_aff_membres(request):
    activites=Activites.objects.all()
    membres=Membres.objects.all()
    verset_bibl=versets.objects.all()
    return render(request,'admin/pages/admin_membre.html',{
        'Activites':activites,
        'Membres':membres,
        'Versets':verset_bibl
    })

def admin_activites(request):
    if request.method=="POST":
        form=CustomActivities(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else: 
        form=CustomActivities()
    activites=Activites.objects.all()
    membres=Membres.objects.all()
    verset_bibl=versets.objects.all()
    return render(request,'admin/pages/admin_activites.html',{
        'Activites':activites,
        'Membres':membres,
        'Versets':verset_bibl,
        'form':form
    })  
 
def admin_versets(request):
    if request.method == "POST":
        form=CustomVersets(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,'Verset ajouté avec succès !')
        return redirect('admin_versets')
    else:
        form=CustomVersets()
    activites=Activites.objects.all()
    membres=Membres.objects.all()
    verset_bibl=versets.objects.all()
    return render(request,'admin/pages/admin_versets.html',{
        'Activites':activites,
        'Membres':membres,
        'Versets':verset_bibl,
        'form':form
    })    
def accueil_view(request):
    activites=Activites.objects.all()
    return render(request, 'pages/index.html',{
        'activite':activites
    })

def Communaute(request):
    return render(request,'pages/Communaute.html')

def Contact(request):
    if request.method == 'POST':
        nom = request.POST.get('name')
        telephone = request.POST.get('num')
        email = request.POST.get('mail')
        adresse = request.POST.get('Ad')
        message = request.POST.get('message')
        
        # Créer et sauvegarder le message en base de données
        Messages.objects.create(
            nom=nom,
            telephone=telephone,
            email=email,
            adresse=adresse,
            message=message
        )
        
        # Redirection ou message de succès
        messages.success(request, 'Votre message a été envoyé avec succès!')
        return redirect('Contact')
    
    return render(request,'pages/Contact.html')

def Politiques(request):
    return render(request,'pages/politiques.html')

def aide(request):
    return render(request,'pages/aide.html')