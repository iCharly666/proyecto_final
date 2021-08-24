"""Gestion_Tareas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from actividades import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="Principal"),
    path('actividades/', views.actividades, name="Actividades"),
    path('formulario/', views.formulario, name="Formulario"),
    path('biblioteca/', views.biblioteca, name="Biblioteca"),
    path('admin_perfil/', views.admin, name="Administrador"),
    path('agregar_actividad/', views.crear, name="Crear"),
    path('perfil/', views.perfil, name="Perfil"),
]
