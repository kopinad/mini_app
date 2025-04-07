# Generated by Django 4.2.20 on 2025-04-06 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0005_remove_review_new_image_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('contact_whatsapp', models.BooleanField(default=False, verbose_name='WhatsApp')),
                ('contact_telegram', models.BooleanField(default=False, verbose_name='Telegram')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.category', verbose_name='Услуга')),
            ],
        ),
    ]
