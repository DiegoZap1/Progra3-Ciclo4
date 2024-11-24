# Generated by Django 5.1.2 on 2024-11-14 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('carnet', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('curso', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estds', models.ManyToManyField(related_name='materias', to='app1.estudiantes')),
            ],
        ),
    ]