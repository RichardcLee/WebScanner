# Generated by Django 2.0.3 on 2018-11-28 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plug', '0013_auto_20181128_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scriptplug',
            name='taken',
        ),
    ]
