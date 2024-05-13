# Generated by Django 5.0.2 on 2024-04-02 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wewindecoration', '0012_remove_order_decorations_order_decorations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='decorations',
        ),
        migrations.AddField(
            model_name='order',
            name='decoration_images',
            field=models.ImageField(default=1, upload_to='order_images/'),
            preserve_default=False,
        ),
    ]
