# Generated by Django 3.1 on 2021-06-15 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarSemestre', '0001_initial'),
        ('gestionarPlanMedicion', '0009_auto_20210615_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planmedicioncurso',
            name='semestre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='gestionarSemestre.semestre'),
        ),
    ]