# Generated by Django 3.0.3 on 2020-05-12 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0007_auto_20200512_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='alunos',
            field=models.ManyToManyField(to='aluno.Aluno'),
        ),
        migrations.RemoveField(
            model_name='dia',
            name='aulas',
        ),
        migrations.AddField(
            model_name='dia',
            name='aulas',
            field=models.ManyToManyField(to='aluno.Aula'),
        ),
    ]
