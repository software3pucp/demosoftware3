# Generated by Django 3.1 on 2021-06-02 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarAcreditadoras', '0002_auto_20210602_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acreditadora',
            name='estado',
            field=models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default=None, max_length=2, null=True),
        ),
    ]
