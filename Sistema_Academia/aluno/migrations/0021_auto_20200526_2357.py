# Generated by Django 3.0.3 on 2020-05-26 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0020_auto_20200525_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='alunos',
            field=models.ManyToManyField(to='aluno.Aluno'),
        ),
    ]