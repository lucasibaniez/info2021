# Generated by Django 3.2.6 on 2021-08-23 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amigos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_area', models.CharField(max_length=4)),
                ('codigo_celular', models.CharField(choices=[('0', '--'), ('15', '15')], max_length=2)),
                ('numero', models.CharField(max_length=15)),
                ('amigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amigos.amigo')),
            ],
            options={
                'db_table': 'telefonos',
            },
        ),
    ]
