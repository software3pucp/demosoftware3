# Generated by Django 3.1 on 2021-07-06 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarFacultad', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('gestionarEspecialidad', '0002_especialidad_estado'),
        ('authentication', '0011_auto_20210706_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserxGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarEspecialidad.especialidad')),
                ('facultad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestionarFacultad.facultad')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='grupos',
        ),
        migrations.DeleteModel(
            name='UserGroups',
        ),
        migrations.AddField(
            model_name='userxgroups',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
