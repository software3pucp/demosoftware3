# Generated by Django 3.1 on 2021-05-15 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarResultados', '0002_auto_20210514_1738'),
        ('gestionarRE', '0003_auto_20210515_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultadoacreditadora',
            name='resultadoPUCP',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarResultados.resultadopucp'),
        ),
    ]
