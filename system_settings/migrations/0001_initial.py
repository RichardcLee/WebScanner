# Generated by Django 2.1.2 on 2018-10-24 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScamSetting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('max_thread', models.IntegerField(default=1)),
                ('weak_password_dict', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SpiderSetting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_start', models.BooleanField(default=False)),
                ('max_thread', models.IntegerField(default=1)),
                ('cms_rule', models.CharField(max_length=256)),
                ('language_rule', models.CharField(max_length=256)),
                ('port_rule', models.CharField(max_length=256)),
            ],
        ),
    ]