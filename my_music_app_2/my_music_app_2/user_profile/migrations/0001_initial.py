# Generated by Django 5.1.2 on 2024-10-20 15:48

import django.core.validators
import my_music_app_2.user_profile.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(15), my_music_app_2.user_profile.validators.username_symbols_validator])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
