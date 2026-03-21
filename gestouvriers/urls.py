from django.urls import path
from . import views
urlpatterns = [
    path('activites/', views.activite, name='voirplus')
]
