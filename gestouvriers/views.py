from django.shortcuts import render
from .models import Activites
def activite(request):
    activite_list=Activites.objects.all()
    return render(request, 'pages/voirplus.html',{'activites':activite_list})

