from django.shortcuts import render
from .models import formation
def formations(request):
    formations=formation.objects.all()
    return render(request, 'pages/voirplus.html',{'formations':formations})
# Create your views here.
