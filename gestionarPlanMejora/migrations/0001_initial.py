# Generated by Django 3.1 on 2021-06-15 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionarHorario', '0001_initial'),
        ('gestionarCurso', '0001_initial'),
        ('gestionarIndicadores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanMejora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default=None, max_length=2, null=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarCurso.curso')),
                ('horario', models.ManyToManyField(to='gestionarHorario.Horario')),
                ('indicador', models.ManyToManyField(to='gestionarIndicadores.Indicador')),
            ],
        ),
    ]
