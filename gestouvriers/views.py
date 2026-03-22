from django.shortcuts import render
from .models import Activites,Membres
def activite(request):
    activite_list=Activites.objects.all()
    return render(request, 'pages/voirplus.html',{'activites':activite_list})
def membre(request):
    membre_list=Membres.objects.all()
    return render(request,'pages/communaute.html',{'membres':membre_list})
