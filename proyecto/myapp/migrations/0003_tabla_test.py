# Generated by Django 4.1.4 on 2022-12-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_noticia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabla_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('columna_uno', models.CharField(max_length=200)),
                ('columna_dos', models.CharField(max_length=200)),
                ('columna_tres', models.CharField(max_length=200)),
                ('columna_cuatro', models.CharField(max_length=200)),
            ],
        ),
    ]
