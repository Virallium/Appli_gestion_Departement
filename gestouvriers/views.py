from django.shortcuts import render
from .models import Activites,Membres,versets
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
    return render(request,'admin/pages/admin.html')

def connexionadmin(request):
    return render(request,'admin/auth/connection.html')

def admin_membres(request):
    return render(request,'admin/pages/admin_membre.html')    

def admin_activites(request):
    return render(request,'admin/pages/admin_activites.html')  
 
def admin_versets(request):
    return render(request,'admin/pages/admin_versets.html')    