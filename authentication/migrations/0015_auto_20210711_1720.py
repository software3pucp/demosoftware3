# Generated by Django 3.1 on 2021-07-11 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_remove_user_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='n_Roles',
            field=models.IntegerField(default=0),
        ),
    ]