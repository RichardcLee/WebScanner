# Generated by Django 2.1.2 on 2018-11-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plug', '0009_plugtype_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='plugtype',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
    ]
