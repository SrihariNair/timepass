# Generated by Django 2.0.6 on 2018-07-18 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20180718_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
