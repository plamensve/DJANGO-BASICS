# Generated by Django 5.1.2 on 2024-10-24 06:38

import django.core.validators
import tasty_recipes_app.user_profile.validators
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
                ('nick_name', models.CharField(unique=True, validators=[django.core.validators.MinLengthValidator(2, message='Nickname must be at least 2 chars long!'), django.core.validators.MaxLengthValidator(15)])),
                ('first_name', models.CharField(validators=[django.core.validators.MaxLengthValidator(30), tasty_recipes_app.user_profile.validators.name_start_with_capital_letter_validator])),
                ('last_name', models.CharField(validators=[django.core.validators.MaxLengthValidator(30), tasty_recipes_app.user_profile.validators.name_start_with_capital_letter_validator])),
                ('chef', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
