# Generated by Django 2.0.6 on 2018-06-27 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180625_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='bootstrap_date',
        ),
    ]