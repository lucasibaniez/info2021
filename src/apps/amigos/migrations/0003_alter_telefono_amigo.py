# Generated by Django 3.2.6 on 2021-08-23 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amigos', '0002_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefono',
            name='amigo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='amigos.amigo'),
        ),
    ]
