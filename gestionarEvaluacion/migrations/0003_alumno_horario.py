# Generated by Django 3.1 on 2021-05-18 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarEvaluacion', '0002_mediciondeindicador'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='horario',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]