# Generated by Django 4.2.20 on 2025-04-04 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dano', models.TextField()),
                ('zadacha', models.TextField()),
                ('sdelano1', models.TextField()),
                ('sdelano2', models.TextField()),
                ('sdelano3', models.TextField()),
                ('img1', models.CharField(max_length=255)),
                ('img2', models.CharField(max_length=255)),
                ('img3', models.CharField(max_length=255)),
                ('img4', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services.category')),
            ],
        ),
    ]
