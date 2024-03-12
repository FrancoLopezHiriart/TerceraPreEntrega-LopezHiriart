from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy

from .models import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Create your views here.

def home (request):
    return render (request, "aplication/equipo_buscar.html")


#___________________Equipo

def equipos (request):
    contexto = {Equipo.objects.all()}
    return render (request, "aplication/equipo_list.html", contexto)

class EquipoList(ListView):
    model = Equipo

class EquipoCreate(CreateView):
    model = Equipo
    fields = ["nombre", "abreviatura", "ciudad"]
    success_url = reverse_lazy("equipos")

class EquipoUpdate(UpdateView):
    model = Equipo
    fields = ["nombre", "abreviatura", "ciudad"]
    success_url = reverse_lazy("equipos")

class EquipoDelete(DeleteView):
    model = Equipo
    success_url = reverse_lazy("equipos")  

def encontrarEquipos(request):
    if request.GET["search"]:
        patron = request.GET["search"]
        equipos = Equipo.objects.filter(ciudad__icontains= patron)
        contexto = {"equipos": equipos}
        return render(request, "aplication/equipo_list.html", contexto)
    
    contexto = {Equipo.objects.all()}
    return render(request, "aplication/equipo_list.html", contexto)   

#___________________Jugadores
    
def jugadores (request):
    contexto = {Jugador.objects.all()}
    return render (request, "aplication/jugador_list.html", contexto)

class JugadorList(ListView):
    model = Jugador

class JugadorCreate(CreateView):
    model = Jugador
    fields = ["nombre", "apellido", "equipo", "edad"]
    success_url = reverse_lazy("jugadores")

class JugadorUpdate(UpdateView):
    model = Jugador
    fields = ["nombre", "apellido", "equipo", "edad"]
    success_url = reverse_lazy("jugadores")

class JugadorDelete(DeleteView):
    model = Jugador
    success_url = reverse_lazy("jugadores")  


#___________________DirectoresTecnicos
    
def directores_tecnicos (request):
    contexto = {DirectorTecnico.objects.all()}
    return render (request, "aplication/directores_tecnicos.html", contexto)

class DirectorTecnicoList(ListView):
    model = DirectorTecnico

class DirectorTecnicoCreate(CreateView):
    model = DirectorTecnico
    fields = ["nombre", "apellido", "email", "equipo"]
    success_url = reverse_lazy("directores_tecnicos")

class DirectorTecnicoUpdate(UpdateView):
    model = DirectorTecnico
    fields = ["nombre", "apellido","email", "equipo"]
    success_url = reverse_lazy("directores_tecnicos")

class DirectorTecnicoDelete(DeleteView):
    model = DirectorTecnico
    success_url = reverse_lazy("directores_tecnicos") 