# Generated by Django 2.2.13 on 2021-04-09 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('partido', models.CharField(max_length=100)),
                ('foto', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
