# Generated by Django 5.0.2 on 2024-03-11 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0010_remove_gallery_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cart',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
