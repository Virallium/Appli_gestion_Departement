from django.urls import path
from . import views
urlpatterns = [
    path('listOuvrier/', views.ouviers_List,name='liste_ourviers')
]
