# Generated by Django 4.1.3 on 2022-12-03 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide')),
                ('title', models.CharField(max_length=100)),
                ('action_name', models.CharField(max_length=100)),
                ('link', models.TextField(blank=True, null=True)),
                ('sub_title', models.CharField(max_length=100)),
            ],
        ),
    ]