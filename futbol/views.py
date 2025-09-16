from django.shortcuts import render, redirect
from .models import EquipoFutbol
from .forms import EquipoFutbolForm, RegistroUsuarioForm
from django.contrib.auth import login

# Home
def home(request):
    return render(request, "home.html")

# Lista de equipos
def lista_equipos(request):
    equipos = EquipoFutbol.objects.all()
    return render(request, "lista_equipos.html", {"equipos": equipos})

# Crear equipo
def crear_equipo(request):
    if request.method == "POST":
        form = EquipoFutbolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_equipos")
    else:
        form = EquipoFutbolForm()
    return render(request, "crear_equipo.html", {"form": form})

# Registro de usuarios
def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("home")
    else:
        form = RegistroUsuarioForm()
    return render(request, "registro.html", {"form": form})

