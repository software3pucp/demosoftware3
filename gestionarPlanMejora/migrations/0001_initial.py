# Generated by Django 3.1 on 2021-06-16 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionarEspecialidad', '0002_especialidad_estado'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadMejora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('descripcion', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EstadoActividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('estado', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PlanMejora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=2, null=True)),
                ('especialidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarEspecialidad.especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='ResponsableMejora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarPlanMejora.actividadmejora')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropuestaMejora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('descripcion', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('estado', models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=2, null=True)),
                ('especialidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarEspecialidad.especialidad')),
                ('planMejora', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarPlanMejora.planmejora')),
            ],
        ),
        migrations.CreateModel(
            name='EvidenciaActividadMejora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, choices=[('0', 'Eliminado'), ('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=2, null=True)),
                ('descripcion', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('concepto', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('archivo', models.FileField(null=True, upload_to='mejora/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarPlanMejora.actividadmejora')),
            ],
        ),
        migrations.AddField(
            model_name='actividadmejora',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarPlanMejora.estadoactividad'),
        ),
        migrations.AddField(
            model_name='actividadmejora',
            name='propuestaMejora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarPlanMejora.propuestamejora'),
        ),
    ]
