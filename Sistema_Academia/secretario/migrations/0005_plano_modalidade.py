# Generated by Django 3.0.3 on 2020-06-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretario', '0004_auto_20200514_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='plano',
            name='modalidade',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]