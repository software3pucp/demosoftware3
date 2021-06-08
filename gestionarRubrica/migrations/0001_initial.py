# Generated by Django 3.1 on 2021-06-08 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionarIndicadores', '0001_initial'),
        ('gestionarEspecialidad', '0001_initial'),
        ('gestionarNivel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubrica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('especialidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionarEspecialidad.especialidad')),
                ('indicador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionarIndicadores.indicador')),
                ('nivel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionarNivel.nivel')),
            ],
        ),
    ]
