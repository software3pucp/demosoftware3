# Generated by Django 3.1 on 2021-06-23 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarPlanMedicion', '0014_auto_20210617_1153'),
        ('gestionarHorario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionarPlanMedicion.planmedicioncurso'),
        ),
    ]
