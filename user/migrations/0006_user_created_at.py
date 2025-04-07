# Generated by Django 4.2.20 on 2025-04-06 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_user_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2023-12-31 23:59:59', verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]
