# Generated by Django 3.1 on 2021-05-13 03:14

from django.db import migrations, models
import gestionarFacultad.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('responsable', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, null=True, upload_to=gestionarFacultad.models.upload_location)),
            ],
        ),
    ]
