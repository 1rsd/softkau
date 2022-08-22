# Generated by Django 4.1 on 2022-08-22 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('Id_interno', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('Apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('Tipo_ID', models.CharField(max_length=10, verbose_name='Tipo_ID')),
                ('Numero_ID', models.CharField(max_length=50, verbose_name='Numero_ID')),
            ],
        ),
    ]