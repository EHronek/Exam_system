# Generated by Django 5.0.7 on 2024-07-27 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0021_alter_exam_model_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 28, 0, 15, 54, 98966)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 28, 0, 15, 54, 98942)),
        ),
    ]