# Generated by Django 3.0.3 on 2020-05-14 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0010_auto_20200514_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='nascimento',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='aula',
            name='alunos',
            field=models.ManyToManyField(to='aluno.Aluno'),
        ),
    ]
