# Generated by Django 4.1.12 on 2023-10-31 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('nomSede', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('direccion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombreUsuario', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
                ('rut', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('passUsuario', models.CharField(max_length=20)),
                ('esConductor', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('modelo', models.CharField(max_length=15)),
                ('marca', models.CharField(max_length=15)),
                ('color', models.CharField(max_length=15)),
                ('anno', models.IntegerField()),
            ],
        ),
    ]