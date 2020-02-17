# Generated by Django 2.1.2 on 2018-10-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plug', '0003_auto_20181025_0556'),
        ('task', '0002_task_port'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='plugs',
        ),
        migrations.AddField(
            model_name='task',
            name='json_plugs',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='plug.JsonPlug'),
        ),
        migrations.AddField(
            model_name='task',
            name='script_plugs',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='plug.ScriptPlug'),
        ),
    ]