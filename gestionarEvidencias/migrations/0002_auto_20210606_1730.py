# Generated by Django 3.1 on 2021-06-06 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarEvidencias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidenciasxhorario',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='archive/'),
        ),
    ]
