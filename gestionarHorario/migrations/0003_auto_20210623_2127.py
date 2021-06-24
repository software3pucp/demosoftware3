# Generated by Django 3.1 on 2021-06-24 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarPlanMedicion', '0016_auto_20210623_1657'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestionarHorario', '0002_auto_20210623_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestionarPlanMedicion.planmedicioncurso'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]