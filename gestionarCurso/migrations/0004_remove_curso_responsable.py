# Generated by Django 3.1 on 2021-07-25 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarCurso', '0003_auto_20210621_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='responsable',
        ),
    ]
