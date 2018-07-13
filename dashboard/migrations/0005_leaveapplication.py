# Generated by Django 2.0.6 on 2018-07-11 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0004_remove_post_text2'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('from_date', models.DateField(default=django.utils.timezone.now)),
                ('to_date', models.DateField(default=django.utils.timezone.now)),
                ('approval', models.CharField(blank=True, choices=[('APPROVED', 'APPROVED'), ('NOT APPROVED', 'NOT APPROVED')], max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]