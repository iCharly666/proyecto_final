# Generated by Django 3.2.4 on 2021-08-25 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0003_auto_20210824_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='descripcion',
            field=models.TextField(null=True, verbose_name='Descripción'),
        ),
    ]
