# Generated by Django 5.1.2 on 2024-11-07 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_user', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='publ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_pub', models.DateField()),
                ('descrip', models.CharField(max_length=300)),
                ('n_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.usrs')),
            ],
        ),
    ]
