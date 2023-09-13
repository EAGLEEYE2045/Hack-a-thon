# Generated by Django 4.2.1 on 2023-09-11 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('case_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cases', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='case',
            name='hearing_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='hearing_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]