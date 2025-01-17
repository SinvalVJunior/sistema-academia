# Generated by Django 3.0.3 on 2020-05-12 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretario', '0003_auto_20200409_1927'),
        ('aluno', '0008_auto_20200512_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='planos',
        ),
        migrations.AddField(
            model_name='aluno',
            name='planos',
            field=models.ManyToManyField(to='secretario.Plano'),
        ),
        migrations.AlterField(
            model_name='aula',
            name='alunos',
            field=models.ManyToManyField(to='aluno.Aluno'),
        ),
    ]
