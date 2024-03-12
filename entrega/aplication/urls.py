from django.urls import path, include
from .views import *

urlpatterns = [
    
    #__________________ Generales

    path('', home, name= "home"),
    path('encontrar_equipos/', encontrarEquipos, name="encontrar_equipos"),
           
    #___________________ Equipos

    path('equipos/', EquipoList.as_view(), name="equipos"), 
    path('equipos_create/', EquipoCreate.as_view(), name="equipos_create"), 
    path('equipos_update/<int:pk>/', EquipoUpdate.as_view(), name="equipos_update"), 
    path('equipos_delete/<int:pk>/', EquipoDelete.as_view(), name="equipos_delete"), 

    #___________________ Jugadores

    path('jugadores/', JugadorList.as_view(), name="jugadores"), 
    path('jugadores_create/', JugadorCreate.as_view(), name="jugadores_create"), 
    path('jugadores_update/<int:pk>/', JugadorUpdate.as_view(), name="jugadores_update"), 
    path('jugadores_delete/<int:pk>/', JugadorDelete.as_view(), name="jugadores_delete"), 

    #___________________ Directores Tecnicos

    path('directores_tecnicos/', DirectorTecnicoList.as_view(), name="directores_tecnicos"), 
    path('directores_tecnicos_create/', DirectorTecnicoCreate.as_view(), name="directores_tecnicos_create"), 
    path('directores_tecnicos_update/<int:pk>/', DirectorTecnicoUpdate.as_view(), name="directores_tecnicos_update"), 
    path('directores_tecnicos_delete/<int:pk>/', DirectorTecnicoDelete.as_view(), name="directores_tecnicos_delete"), 

]