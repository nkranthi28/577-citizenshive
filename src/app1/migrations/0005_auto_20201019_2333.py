# Generated by Django 3.1.2 on 2020-10-20 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20201019_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='caregiver',
            name='availability',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='bio',
            field=models.TextField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='city',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='state',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='zip_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 19, 23, 33, 49, 786491)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 19, 23, 33, 49, 786491)),
        ),
    ]
