# Generated by Django 2.2.13 on 2021-04-10 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jherson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='imagen',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
