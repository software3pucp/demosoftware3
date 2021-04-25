# Generated by Django 2.2.13 on 2021-04-25 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageLearned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(default=0)),
                ('id_language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='leon.Language')),
            ],
        ),
    ]
