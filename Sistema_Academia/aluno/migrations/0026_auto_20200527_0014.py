# Generated by Django 3.0.3 on 2020-05-27 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0025_auto_20200527_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='alunos',
            field=models.ManyToManyField(to='aluno.Aluno'),
        ),
    ]