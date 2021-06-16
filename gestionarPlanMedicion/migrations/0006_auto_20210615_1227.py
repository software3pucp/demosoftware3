# Generated by Django 3.1 on 2021-06-15 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarEspecialidad', '0002_especialidad_estado'),
        ('gestionarSemestre', '0001_initial'),
        ('gestionarPlanMedicion', '0005_auto_20210615_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanMedicionHistorico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo')], default=None, max_length=2, null=True)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarEspecialidad.especialidad')),
                ('semestre', models.ManyToManyField(to='gestionarSemestre.Semestre')),
            ],
        ),
        migrations.AlterField(
            model_name='planmedicioncurso',
            name='planMedicion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarPlanMedicion.planmedicionhistorico'),
        ),
    ]