# Generated by Django 3.1.1 on 2024-03-25 12:45

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('podcast_detail', '0005_auto_20240325_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='author',
            field=models.ForeignKey(blank=True, default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]