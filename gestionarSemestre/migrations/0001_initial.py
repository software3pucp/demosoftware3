# Generated by Django 3.1 on 2021-05-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCodigo', models.CharField(max_length=10)),
                ('anho', models.IntegerField()),
                ('etapa', models.IntegerField()),
                ('inicio', models.DateTimeField(blank=True, null=True)),
                ('fin', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
