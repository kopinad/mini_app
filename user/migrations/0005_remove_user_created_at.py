# Generated by Django 4.2.20 on 2025-04-06 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
    ]
