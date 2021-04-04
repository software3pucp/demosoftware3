# Generated by Django 2.2.13 on 2021-04-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('longitud', models.IntegerField(default=0)),
                ('habloElIdioma', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
