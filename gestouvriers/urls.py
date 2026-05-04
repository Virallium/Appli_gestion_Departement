from django.urls import path
from . import views
urlpatterns = [
    path('activites/', views.activite, name='voirplus'),
    path('Communaute/', views.membre, name='Communaute'),
    path('Administrateur/', views.admin, name='Admin'),
    path('Admin_connexion/',views.connexionadmin, name="admin_connexion"),
    path('LoginAdmin/', views.connexionadmin, name="loginAdmin"),
    path('ChangerMotDePasse/', views.changempass, name="changer_mp"),
    path('Membres enregistres/',views.admin_aff_membres, name="admin_membres"),
    path('Activites/',views.admin_activites, name="admin_activites"),
    path('Versets biblique/',views.admin_versets, name="admin_versets"),
]
