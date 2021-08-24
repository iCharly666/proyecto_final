from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def principal(request):
    return render(request, "actividades/principal.html")


def actividades(request):
    return render(request, "actividades/actividades.html")


def formulario(request):
    return render(request, "actividades/formulario.html")


def biblioteca(request):
    return render(request, "actividades/biblioteca.html")


def admin(request):
    return render(request, "actividades/admin_perfil.html")


def crear(request):
    return render(request, "actividades/agregar_actividad.html")


def perfil(request):
    return render(request, "actividades/perfil.html")
