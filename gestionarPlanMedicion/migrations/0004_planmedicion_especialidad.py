# Generated by Django 3.1 on 2021-06-15 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarEspecialidad', '0002_especialidad_estado'),
        ('gestionarPlanMedicion', '0003_auto_20210615_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='planmedicion',
            name='especialidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestionarEspecialidad.especialidad'),
        ),
    ]
