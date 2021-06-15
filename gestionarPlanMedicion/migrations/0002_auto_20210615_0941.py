# Generated by Django 3.1 on 2021-06-15 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarIndicadores', '0001_initial'),
        ('gestionarCurso', '0001_initial'),
        ('gestionarSemestre', '0001_initial'),
        ('gestionarHorario', '0001_initial'),
        ('gestionarPlanMedicion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planmedicion',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='planmedicion',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='planmedicion',
            name='indicador',
        ),
        migrations.AddField(
            model_name='planmedicion',
            name='nombre',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='planmedicion',
            name='semestre',
            field=models.ManyToManyField(to='gestionarSemestre.Semestre'),
        ),
        migrations.AlterField(
            model_name='planmedicion',
            name='estado',
            field=models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo')], default=None, max_length=2, null=True),
        ),
        migrations.CreateModel(
            name='PlanMedicionCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default=None, max_length=2, null=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarCurso.curso')),
                ('horario', models.ManyToManyField(to='gestionarHorario.Horario')),
                ('indicador', models.ManyToManyField(to='gestionarIndicadores.Indicador')),
                ('planMedicion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarPlanMedicion.planmedicion')),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarSemestre.semestre')),
            ],
        ),
    ]
