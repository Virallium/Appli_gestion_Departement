from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('Accueil/', views.accueil_view, name='Accueil'),
    path('Communaute/', views.Communaute, name='Communaute'),
    path('Contact/', views.Contact, name='Contact'),
    path('Politiques/',views.Politiques, name='Politiques' ),
    path('Aide/', views.aide, name='Aide'),
    path('activites/',include('gestouvriers.urls'))
]
