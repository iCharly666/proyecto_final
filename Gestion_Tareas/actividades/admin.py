from django.contrib import admin
from .models import Tareas
from .models import Comentario
from .models import Bibliotecas

# Register your models here.


class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('materia', 'actividad', 'descripcion', 'entrega')
    search_fields = ('materia', 'actividad', 'descripcion', 'entrega')
    date_hierarchy = 'created'
    list_filter = ('materia', 'actividad')


admin.site.register(Tareas, AdministrarModelo)


class AdminComentarios(admin.ModelAdmin):
    list_display = ('id', 'materia')
    search_fields = ('id', 'materia', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id', 'materia')


admin.site.register(Comentario, AdminComentarios)


class AdministrarModelo2(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'editorial', 'nombre', 'uploadedFile')
    search_fields = ('id', 'editorial', 'nombre', 'uploadedFile')
    date_hierarchy = 'created'
    list_filter = ('editorial', 'nombre')


admin.site.register(Bibliotecas, AdministrarModelo2)
