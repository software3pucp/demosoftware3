# Generated by Django 3.1 on 2021-07-08 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarREAcreditadoras', '0011_historiareacred'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiareacred',
            name='especialidad',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='historiareacred',
            name='facultad',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
    ]
