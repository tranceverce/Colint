# Generated by Django 4.1.5 on 2023-04-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Admin', '0004_item_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
