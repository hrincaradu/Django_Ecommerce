# Generated by Django 4.1.3 on 2022-12-03 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_slider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='action_name',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='link',
        ),
    ]
