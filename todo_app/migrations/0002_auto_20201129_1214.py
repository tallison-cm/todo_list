# Generated by Django 3.1.3 on 2020-11-29 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listatarefas',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 12, 14, 42, 350131)),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 12, 14, 42, 385154)),
        ),
    ]
