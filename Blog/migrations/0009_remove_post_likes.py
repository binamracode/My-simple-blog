# Generated by Django 3.0.8 on 2020-07-21 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_auto_20200721_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
