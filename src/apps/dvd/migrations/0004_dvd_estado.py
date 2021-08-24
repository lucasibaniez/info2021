# Generated by Django 3.2.6 on 2021-08-24 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvd', '0003_auto_20210823_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='dvd',
            name='estado',
            field=models.CharField(choices=[('A', 'ACTIVO'), ('I', 'INACTIVO')], default='A', max_length=1),
        ),
    ]
