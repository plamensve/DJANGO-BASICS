# Generated by Django 5.1.2 on 2024-10-10 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('date_time_of_publication', models.DateTimeField(auto_now_add=True)),
                ('to_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_to_photo', to='photos.photo')),
            ],
            options={
                'ordering': ['-date_time_of_publication'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_to_photo', to='photos.photo')),
            ],
        ),
    ]
