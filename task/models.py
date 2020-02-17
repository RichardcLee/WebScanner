from django.db import models


# Create your models here.


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    # 任务名称
    name = models.CharField(max_length=256)
    run_times_choices = (
        ('0', '每天'),
        ('1', '每周一次'),
        ('2', '每月一次')
    )
    # 执行周期
    run_times = models.CharField(choices=run_times_choices,
                                 default='0',
                                 max_length=32)
    # 是否自动刷新列表
    is_auto_flush = models.BooleanField(default=False)
    # 任务类型
    task_type = models.CharField(max_length=256)
    crisis_level_choices = (
        ('0', '高危'),
        ('1', '危险'),
        ('2', '中等'),
        ('3', '普通')
    )
    # 危害等级
    crisis_level = models.CharField(choices=crisis_level_choices,
                                    default="0",
                                    max_length=32)
    # 插件选择
    json_plugs = models.ManyToManyField('plug.JsonPlug',
                                        blank=True,
                                        default=None)
    script_plugs = models.ManyToManyField('plug.ScriptPlug',
                                          blank=True,
                                          default=None)
    # 目标地址
    target = models.CharField(max_length=256)
    # 目标端口
    port = models.IntegerField(default=80)
