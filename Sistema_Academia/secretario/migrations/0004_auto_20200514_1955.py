# Generated by Django 3.0.3 on 2020-05-14 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretario', '0003_auto_20200409_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plano',
            old_name='name',
            new_name='nome',
        ),
    ]
