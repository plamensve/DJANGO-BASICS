# Generated by Django 5.0.4 on 2024-09-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_personinfor_stats'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentWithChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(blank=True, null=True)),
                ('status', models.CharField(choices=[(1, 'DRAFT'), (2, 'PUBLISHED'), (3, 'ARCHIVED')])),
            ],
        ),
    ]
