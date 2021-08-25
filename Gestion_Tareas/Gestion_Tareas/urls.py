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
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from actividades import views
from django.conf import settings

from actividades import views as views_actividades
# Importamos la nueva vista de app registros para poder asignar las rutas de acceso a sus vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="Principal"),
    path('actividades/', views_actividades.actividades, name="Actividades"),
    path('formulario/', views_actividades.formulario, name="Formulario"),
    path('registrar/', views_actividades.registrar, name="Registrar"),
    path('biblioteca/', views_actividades.biblioteca, name="Biblioteca"),
    path('admin_perfil/', views_actividades.admin, name="Consultar"),
    path('agregar_actividad/', views.crear, name="Crear"),
    path('perfil/', views.perfil, name="Perfil"),
    path('eliminarComentario/<int:id>/',
         views_actividades.eliminarComentario,
         name='Eliminar'),
    path('FormEditarComentario/<int:id>/',
         views_actividades.consultarComentarioIndividual,
         name='ConsultaIndividual'),
    path('editarComentario/<int:id>/',
         views_actividades.editarComentarioContacto, name='Editar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
