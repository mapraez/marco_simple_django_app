# Generated by Django 3.2 on 2021-05-09 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reskill_america_django_app', '0003_auto_20210509_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Certificate_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reskill_america_django_app.certificate_type'),
        ),
        migrations.AddField(
            model_name='student',
            name='Department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reskill_america_django_app.department'),
        ),
        migrations.AddField(
            model_name='student',
            name='Grade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reskill_america_django_app.grade'),
        ),
        migrations.AddField(
            model_name='student',
            name='School',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reskill_america_django_app.school'),
        ),
    ]
