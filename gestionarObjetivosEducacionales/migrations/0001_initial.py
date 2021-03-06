# Generated by Django 3.1 on 2021-07-07 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionarEspecialidad', '0002_especialidad_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjetivoEducacional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('descripcion', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('estado', models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=2, null=True)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarEspecialidad.especialidad')),
            ],
        ),
    ]
