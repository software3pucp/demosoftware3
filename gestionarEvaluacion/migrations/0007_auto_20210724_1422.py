# Generated by Django 3.1 on 2021-07-24 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarHorario', '0006_auto_20210707_1733'),
        ('gestionarEvaluacion', '0006_auto_20210723_1252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='respuestaevaluacion',
            options={'ordering': ['codigoAlumno']},
        ),
        migrations.RemoveField(
            model_name='respuestaevaluacion',
            name='alumno',
        ),
        migrations.AddField(
            model_name='respuestaevaluacion',
            name='codigoAlumno',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='respuestaevaluacion',
            name='horario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestionarHorario.horario'),
        ),
        migrations.AddField(
            model_name='respuestaevaluacion',
            name='nombreAlumno',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mediciondeindicador',
            name='alumno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestionarEvaluacion.respuestaevaluacion'),
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
    ]
