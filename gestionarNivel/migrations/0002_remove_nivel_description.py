# Generated by Django 3.1 on 2021-05-11 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarNivel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nivel',
            name='description',
        ),
    ]
