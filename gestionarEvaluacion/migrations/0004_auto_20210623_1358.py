# Generated by Django 3.1 on 2021-06-23 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarEvaluacion', '0003_respuestaevaluacion_indicador'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mediciondeindicador',
            options={'ordering': ['codigo']},
        ),
        migrations.AlterModelOptions(
            name='respuestaevaluacion',
            options={'ordering': ['codigoAlumno']},
        ),
    ]
