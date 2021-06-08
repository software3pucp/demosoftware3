# Generated by Django 3.1 on 2021-06-08 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionarAcreditadoras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadoAcreditadora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('descripcion', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('estado', models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default='2', max_length=2, null=True)),
                ('acreditadora', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestionarAcreditadoras.acreditadora')),
            ],
        ),
    ]
