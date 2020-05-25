# Generated by Django 3.0.3 on 2020-05-25 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
        ('aluno', '0017_auto_20200525_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='treino',
            field=models.ManyToManyField(default=None, to='professor.Treino'),
        ),
        migrations.AlterField(
            model_name='aula',
            name='alunos',
            field=models.ManyToManyField(to='aluno.Aluno'),
        ),
    ]
