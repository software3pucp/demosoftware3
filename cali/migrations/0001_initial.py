# Generated by Django 2.2.13 on 2021-04-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nombCandidato', models.CharField(max_length=150)),
                ('postura', models.CharField(max_length=150)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]