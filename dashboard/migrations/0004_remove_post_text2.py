# Generated by Django 2.0.6 on 2018-07-09 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_post_text2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text2',
        ),
    ]