# Generated by Django 5.0.4 on 2024-09-30 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_studentwithchoices_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentWithChoices',
        ),
        migrations.RemoveField(
            model_name='personinfor',
            name='stats',
        ),
    ]
