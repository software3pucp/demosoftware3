# Generated by Django 3.1 on 2021-05-11 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarRE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultadoacreditadora',
            name='codigo',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
