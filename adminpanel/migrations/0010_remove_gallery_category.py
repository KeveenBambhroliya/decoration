# Generated by Django 5.0.2 on 2024-03-11 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0009_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='category',
        ),
    ]
