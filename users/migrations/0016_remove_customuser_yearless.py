# Generated by Django 2.0.6 on 2018-07-01 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_customuser_yearless'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='yearless',
        ),
    ]