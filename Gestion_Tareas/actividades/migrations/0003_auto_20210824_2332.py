# Generated by Django 3.2.4 on 2021-08-25 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0002_auto_20210824_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tareas',
            name='carrera',
        ),
        migrations.RemoveField(
            model_name='tareas',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='tareas',
            name='duracion',
        ),
        migrations.RemoveField(
            model_name='tareas',
            name='hora',
        ),
        migrations.RemoveField(
            model_name='tareas',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='tareas',
            name='nombre',
        ),
        migrations.AddField(
            model_name='tareas',
            name='actividad',
            field=models.TextField(max_length=12, null=True, verbose_name='Actividad'),
        ),
        migrations.AddField(
            model_name='tareas',
            name='descripcion',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='tareas',
            name='entrega',
            field=models.CharField(max_length=10, null=True, verbose_name='Fecha'),
        ),
        migrations.AddField(
            model_name='tareas',
            name='materia',
            field=models.TextField(null=True, verbose_name='Materia'),
        ),
    ]