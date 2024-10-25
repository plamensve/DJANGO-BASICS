# Generated by Django 5.1.2 on 2024-10-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image_url',
            field=models.URLField(error_messages={'unique': 'This image URL is already in use! Provide a new one.'}, unique=True),
        ),
    ]
