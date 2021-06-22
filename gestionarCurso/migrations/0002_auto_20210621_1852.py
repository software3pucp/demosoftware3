# Generated by Django 3.1 on 2021-06-21 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarCurso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='estado',
            field=models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default=None, max_length=50, null=True),
        ),
    ]
