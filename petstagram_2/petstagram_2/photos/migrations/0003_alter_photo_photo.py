# Generated by Django 5.1.2 on 2024-10-10 10:11

import petstagram_2.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_comment_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='images', validators=[petstagram_2.photos.validators.photo_size_validator]),
        ),
    ]
