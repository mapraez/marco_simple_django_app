# Generated by Django 3.2 on 2021-05-09 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reskill_america_django_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_of_resumption',
        ),
        migrations.AlterField(
            model_name='student',
            name='grad_year',
            field=models.IntegerField(),
        ),
    ]
