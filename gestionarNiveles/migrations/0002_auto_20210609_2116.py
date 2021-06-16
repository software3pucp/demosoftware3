# Generated by Django 3.1 on 2021-06-10 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarEspecialidad', '0002_especialidad_estado'),
        ('gestionarNiveles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nivel',
            old_name='value',
            new_name='valor',
        ),
        migrations.RemoveField(
            model_name='nivel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='nivel',
            name='state',
        ),
        migrations.AddField(
            model_name='nivel',
            name='especialidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarEspecialidad.especialidad'),
        ),
        migrations.AddField(
            model_name='nivel',
            name='estado',
            field=models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='nivel',
            name='nombre',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]