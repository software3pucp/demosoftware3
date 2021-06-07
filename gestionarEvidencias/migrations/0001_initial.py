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
            name='EvidenciasxHorario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=2, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archive/')),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarHorario.horario')),
            ],
        ),
    ]
