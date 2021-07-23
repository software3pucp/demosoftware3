# Generated by Django 3.1 on 2021-07-23 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarHorario', '0006_auto_20210707_1733'),
        ('gestionarEvaluacion', '0005_respuestaevaluacion_planmedicion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='respuestaevaluacion',
            options={},
        ),
        migrations.RemoveField(
            model_name='respuestaevaluacion',
            name='codigoAlumno',
        ),
        migrations.RemoveField(
            model_name='respuestaevaluacion',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='respuestaevaluacion',
            name='nombreAlumno',
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAlumno', models.CharField(blank=True, max_length=10, null=True)),
                ('codigoAlumno', models.CharField(blank=True, max_length=9, null=True)),
                ('horario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarHorario.horario')),
            ],
        ),
        migrations.AddField(
            model_name='respuestaevaluacion',
            name='alumno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarEvaluacion.alumno'),
        ),
        migrations.AlterField(
            model_name='mediciondeindicador',
            name='alumno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestionarEvaluacion.alumno'),
        ),
    ]
