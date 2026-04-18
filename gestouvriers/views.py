from django.shortcuts import render,redirect
from .models import Activites,Membres,versets
from django.contrib import messages
from .form import CustomMembers, CustomActivities, CustomVersets
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
    return render(request,'admin/auth/connection.html')
#change password admin
def changempass(request):
    return render(request,'admin/auth/changempass.html')

def admin_membres(request):
    if request.method=="POST":
        form=CustomMembers(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Membre ajouté avec succès !')
            return redirect('admin_membres')
    else:
        form=CustomMembers()
    activites=Activites.objects.all()
    membres=Membres.objects.all()
    verset_bibl=versets.objects.all()
    return render(request,'admin/pages/admin_membre.html',{
        'form':form,
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