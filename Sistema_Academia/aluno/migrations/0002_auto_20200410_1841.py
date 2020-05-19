# Generated by Django 3.0.4 on 2020-04-10 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretario', '0003_auto_20200409_1927'),
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='nome',
            new_name='name',
        ),
        migrations.AddField(
            model_name='aluno',
            name='email',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='planos',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='secretario.Plano'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='senha',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('modalidade', models.CharField(max_length=100)),
                ('horario', models.CharField(max_length=100)),
                ('max_alunos', models.IntegerField()),
                ('alunos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.Aluno')),
            ],
        ),
    ]