# Generated by Django 5.0.4 on 2024-09-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
