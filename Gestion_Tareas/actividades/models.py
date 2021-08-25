from django.db import models

# Create your models here.


class Tareas(models.Model):
    materia = models.TextField(null=True, verbose_name="Materia")
    actividad = models.TextField(
        null=True, max_length=100, verbose_name="Actividad")
    descripcion = models.TextField(
        null=True, verbose_name="Descripción")
    #imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    entrega = models.CharField(
        null=True, max_length=10, verbose_name="Fecha")
    created = models.DateTimeField(null=True, auto_now_add=True)
    updated = models.DateTimeField(null=True, auto_now_add=True)

    readonly_fields = ('created', 'updated')

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ["created"]

    def __str__(self):
        return self.materia


class Comentario(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="Clave")
    materia = models.TextField(verbose_name="Materia")
    mensaje = models.TextField(verbose_name="Descripción")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Registrado")

    class Meta:

        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]

    def str(self):

        return self.mensaje
    # Indica que se mostrára el mensaje como valor en la tabla


class Bibliotecas(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    editorial = models.TextField(
        null=True, max_length=100, verbose_name="Nombre Editorial")
    nombre = models.TextField(
        null=True, verbose_name="Nombre Libro")
    #imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    uploadedFile = models.FileField(upload_to="Uploaded Files/")
    created = models.DateTimeField(null=True, auto_now_add=True)
    updated = models.DateTimeField(null=True, auto_now_add=True)

    readonly_fields = ('created', 'updated')

    class Meta:
        verbose_name = "Biblioteca"
        verbose_name_plural = "Bibliotecas"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
