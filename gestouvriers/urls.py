from django.urls import path
from . import views
urlpatterns = [
    path('activites/', views.activite, name='voirplus'),
    path('Communaute/', views.membre, name='Communaute'),
    path('Administrateur/', views.admin, name='Admin'),
    path('LoginAdmin/', views.connexionadmin, name="loginAdmin"),
    path('Membres enregistres/',views.admin_membres, name="admin_membres"),
    path('Activites/',views.admin_activites, name="admin_activites"),
    path('Versets biblique/',views.admin_versets, name="admin_versets"),
]
