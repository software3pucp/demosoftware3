# Generated by Django 3.1 on 2021-06-07 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionarHorario', '0005_delete_evidenciasxhorario'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicionDeIndicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('resultado', models.CharField(blank=True, default='', max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaEvaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAlumno', models.CharField(blank=True, max_length=10, null=True)),
                ('codigoAlumno', models.CharField(blank=True, max_length=9, null=True)),
                ('descripcionP', models.CharField(blank=True, max_length=200)),
                ('valorNota', models.IntegerField(null=True)),
                ('estado', models.CharField(default=1, max_length=2)),
                ('calificado', models.CharField(default=0, max_length=2, null=True)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarHorario.horario')),
            ],
        ),
    ]
