# Generated by Django 3.1 on 2021-05-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarEvaluacion', '0005_auto_20210519_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='estado',
            field=models.CharField(default=1, max_length=2),
        ),
    ]