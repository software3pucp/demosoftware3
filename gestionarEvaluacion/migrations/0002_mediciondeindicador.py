# Generated by Django 3.1 on 2021-05-15 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarCurso', '0001_initial'),
        ('gestionarSemestre', '0007_auto_20210511_2341'),
        ('gestionarEvaluacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicionDeIndicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('resultado', models.CharField(blank=True, default='', max_length=4, null=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarEvaluacion.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarCurso.curso')),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarSemestre.semestre')),
            ],
        ),
    ]
