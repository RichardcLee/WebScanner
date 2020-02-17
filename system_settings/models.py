from django.db import models


# Create your models here.

class SpiderSetting(models.Model):
    id = models.AutoField(primary_key=True)
    is_start = models.BooleanField(default=False)
    max_thread = models.IntegerField(default=1)
    cms_rule = models.CharField(max_length=256)
    language_rule = models.CharField(max_length=256)
    port_rule = models.CharField(max_length=256)


class ScamSetting(models.Model):
    id = models.AutoField(primary_key=True)
    max_thread = models.IntegerField(default=1)
    weak_password_dict = models.TextField()
