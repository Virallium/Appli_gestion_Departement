from django.shortcuts import render
def login_view(request):
    return render(request, 'auth/login.html')

def register_view(request):
    return render(request, 'auth/register.html')
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

