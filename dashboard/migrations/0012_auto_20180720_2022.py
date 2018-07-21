# Generated by Django 2.0.6 on 2018-07-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='approval',
            field=models.CharField(blank=True, choices=[('APPROVAL PENDING', 'APPROVAL PENDING'), ('APPROVED', 'APPROVED'), ('NOT APPROVED', 'NOT APPROVED')], default='APPROVAL PENDING', max_length=100),
        ),
    ]