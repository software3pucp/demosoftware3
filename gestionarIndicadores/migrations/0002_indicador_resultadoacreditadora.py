# Generated by Django 3.1 on 2021-07-06 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarREAcreditadoras', '0010_remove_resultadoacreditadora_indicador'),
        ('gestionarIndicadores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador',
            name='resultadoAcreditadora',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionarREAcreditadoras.resultadoacreditadora'),
        ),
    ]
