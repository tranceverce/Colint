# Generated by Django 4.1.5 on 2023-02-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feed',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('bad', models.PositiveIntegerField()),
                ('good', models.PositiveIntegerField()),
                ('best', models.PositiveIntegerField()),
            ],
        ),
    ]