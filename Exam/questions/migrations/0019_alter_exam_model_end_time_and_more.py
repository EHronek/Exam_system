# Generated by Django 5.0.7 on 2024-07-27 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_alter_exam_model_end_time_alter_exam_model_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 27, 19, 3, 57, 955885)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 27, 19, 3, 57, 955769)),
        ),
    ]
