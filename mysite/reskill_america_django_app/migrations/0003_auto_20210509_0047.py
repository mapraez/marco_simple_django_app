# Generated by Django 3.2 on 2021-05-09 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reskill_america_django_app', '0002_auto_20210509_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='date_of_resumption',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_resumption',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]