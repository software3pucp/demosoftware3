# Generated by Django 3.1 on 2021-06-08 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarAcreditadoras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acreditadora',
            name='estado',
            field=models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=2, null=True),
        ),
    ]