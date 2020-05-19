# Generated by Django 3.0.3 on 2020-05-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0014_auto_20200518_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='dia',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='aula',
            name='alunos',
            field=models.ManyToManyField(to='aluno.Aluno'),
        ),
    ]