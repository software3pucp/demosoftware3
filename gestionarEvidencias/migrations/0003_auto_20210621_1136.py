# Generated by Django 3.1 on 2021-06-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarEvidencias', '0002_evidenciasxhorario_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidenciasxhorario',
            name='concepto',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='evidenciasxhorario',
            name='descripcion',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
