# Generated by Django 3.1 on 2021-05-18 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionarIndicadores', '0002_auto_20210515_1658'),
        ('gestionarCurso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanMedicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default=None, max_length=2, null=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarCurso.curso')),
                ('indicador', models.ManyToManyField(to='gestionarIndicadores.Indicador')),
            ],
        ),
    ]
