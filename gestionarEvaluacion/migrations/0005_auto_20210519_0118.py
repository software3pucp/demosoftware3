# Generated by Django 3.1 on 2021-05-19 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarEvaluacion', '0004_alumno_puntuacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='puntuacion',
        ),
        migrations.AddField(
            model_name='alumno',
            name='descripcionP',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
