# Generated by Django 3.0.3 on 2020-05-27 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0028_auto_20200527_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='alunos',
            field=models.ManyToManyField(to='aluno.Aluno'),
        ),
    ]
