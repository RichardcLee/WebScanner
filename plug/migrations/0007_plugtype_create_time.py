# Generated by Django 2.1.2 on 2018-11-01 11:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plug', '0006_auto_20181101_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='plugtype',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
