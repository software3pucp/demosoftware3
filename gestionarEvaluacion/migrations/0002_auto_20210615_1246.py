# Generated by Django 3.1 on 2021-06-15 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionarSemestre', '0001_initial'),
        ('gestionarRubrica', '__first__'),
        ('gestionarCurso', '0001_initial'),
        ('gestionarEvaluacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediciondeindicador',
            name='alumno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestionarEvaluacion.respuestaevaluacion'),
        ),
        migrations.AddField(
            model_name='mediciondeindicador',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestionarCurso.curso'),
        ),
        migrations.AddField(
            model_name='mediciondeindicador',
            name='semestre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestionarSemestre.semestre'),
        ),
        migrations.AddField(
            model_name='respuestaevaluacion',
            name='rubrica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestionarRubrica.rubrica'),
        ),
    ]