# Generated by Django 3.2.4 on 2021-08-25 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0006_biblioteca'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='biblioteca',
            new_name='Bibliotecas',
        ),
        migrations.AlterModelOptions(
            name='bibliotecas',
            options={'ordering': ['-created'], 'verbose_name': 'Biblioteca', 'verbose_name_plural': 'Bibliotecas'},
        ),
    ]
