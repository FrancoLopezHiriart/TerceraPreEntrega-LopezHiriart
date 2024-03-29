# Generated by Django 5.0.2 on 2024-03-09 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DirectorTecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('equipo', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'DirectorTecnico',
                'verbose_name_plural': 'DirectoresTecnicos',
                'ordering': ['nombre', 'apellido'],
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('abreviatura', models.CharField(max_length=6)),
                ('ciudad', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ['-nombre'],
            },
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('equipo', models.CharField(max_length=60)),
                ('edad', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
                'ordering': ['nombre', 'apellido'],
            },
        ),
    ]
