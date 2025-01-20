# Generated by Django 4.2.18 on 2025-01-20 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='ModuleCourse',
            name='id',
        ),
        migrations.AddField(
            model_name='ModuleCourse',
            name='name',
            field=models.ManyToManyField(to='management.course'),
        ),
        migrations.AddField(
            model_name='ModuleCourse',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='module',
            name='category',
            field=models.CharField(choices=[('compulsary', 'compulsary'), ('voluntary', 'voluntary')], max_length=30),
        ),
        migrations.AlterField(
            model_name='registration',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]
