# Generated by Django 2.0.6 on 2018-07-01 14:48

import datetime
from django.db import migrations
import djangoyearlessdate.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20180630_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='yearless',
            field=djangoyearlessdate.models.YearlessDateField(default=datetime.date.today, max_length=4),
        ),
    ]
