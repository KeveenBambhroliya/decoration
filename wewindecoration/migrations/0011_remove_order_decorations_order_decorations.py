# Generated by Django 5.0.2 on 2024-04-02 01:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0018_decoration'),
        ('wewindecoration', '0010_remove_order_decoration_order_decorations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='decorations',
        ),
        migrations.AddField(
            model_name='order',
            name='decorations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminpanel.decoration'),
        ),
    ]
