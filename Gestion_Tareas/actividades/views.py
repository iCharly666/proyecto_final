from django.shortcuts import render
from django.http import HttpResponse
from .models import Tareas
from .forms import ComentarioForm
from .models import Comentario
from .models import Bibliotecas
from django.shortcuts import get_object_or_404

# Create your views here.


def principal(request):
    return render(request, "actividades/principal.html")


def actividades(request):
    tareas = Tareas.objects.all()
    return render(request, "actividades/actividades.html", {'tareas': tareas})
    # all recupera todos los objetos del modelo (registros de la tabla alumnos)
    # Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados


def registrar(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():  # Si los datos recibidos son correctos
            form.save()  # inserta
            comentarios = Comentario.objects.all()
            return render(request, "actividades/admin_perfil.html",
                          {'comentarios': comentarios})
            return render(request, 'actividades/formulario.html')
    form = ComentarioForm()
    # Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request, 'actividades/formulario.html', {'form': form})


def eliminarComentario(request, id,
                       confirmacion='actividades/confirmarEliminacion.html'):
    comentario = get_object_or_404(Comentario, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = Comentario.objects.all()
        return render(request, "actividades/admin_perfil.html",
                      {'comentarios': comentarios})
    return render(request, confirmacion, {'object': comentario})


def consultarComentarioIndividual(request, id):
    comentario = Comentario.objects.get(id=id)
    # get permite establecer una condicionante a la consulta y recupera el objetos
    # del modelo que cumple la condición (registro de la tabla ComentariosContacto.
    # get se emplea cuando se sabe que solo hay un objeto que coincide con su
    # consulta.
    return render(request, "actividades/FormEditarComentario.html",
                  {'comentario': comentario})
    # Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados.


def editarComentarioContacto(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    form = ComentarioForm(request.POST, instance=comentario)
    # Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if form.is_valid():
        form.save()  # si el registro ya existe, se modifica.
    comentarios = Comentario.objects.all()
    return render(request, "actividades/admin_perfil.html",
                  {'comentarios': comentarios})
    # Si el formurio no es valido nos regresa al formulario para verificar
    # datos
    return render(request, "actividades/admin_perfil.html",
                  {'comentario': comentario})


def formulario(request):
    return render(request, "actividades/formulario.html")


def biblioteca(request):
    bibliotecas = Bibliotecas.objects.all()
    return render(request, "actividades/biblioteca.html", {'bibliotecas': bibliotecas})


def admin(request):
    return render(request, "actividades/admin_perfil.html")


def consultarComentario(request):
    comentarios = Comentario.objects.all()
    # all recupera todos los objetos del modelo (registros de la tabla
    # comentariosContacto)
    return render(request, "actividades/admin_perfil.html",
                  {'comentarios': comentarios})
    # Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de comentarios recuparados.


def crear(request):
    return render(request, "actividades/agregar_actividad.html")


def perfil(request):
    return render(request, "actividades/perfil.html")
