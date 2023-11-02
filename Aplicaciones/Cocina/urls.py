from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('index/', views.index),
    path('gestionRecetas/', views.gestionRecetas),
    path('registrarReceta/', views.registrarReceta),
    path('editarReceta/<id>', views.editarReceta),
    path('edicionReceta/', views.edicionReceta),
    path('eliminarReceta/<id>', views.eliminarReceta),
    path('base/', views.base),
    path('receta/<id>', views.receta),
    path('buscar/', views.buscarReceta, name='buscarReceta'),
    
]  