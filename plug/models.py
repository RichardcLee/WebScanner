from django.db import models


# Create your models here.

class JsonPlug(models.Model):
    """
    json插件类
    """
    id = models.AutoField(primary_key=True)
    # 插件类型
    plug_type = models.ForeignKey('PlugType',
                                  on_delete=models.DO_NOTHING,
                                  related_name='json_plug')
    # 插件名称
    name = models.CharField(max_length=256,
                            null=False,
                            blank=False)
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
    # 插件说明
    info = models.CharField(max_length=256,
                            default="",
                            null=True)
    # 插件作者
    author = models.CharField(max_length=256)
    # 插件链接
    plug_url = models.URLField()
    analyzing_type_choices = (
        ('0', '正则表达式'),
        ('1', '关键字'),
        ('2', 'MD5')
    )
    # 分析方式
    analyzing_type = models.CharField(choices=analyzing_type_choices,
                                      default='0',
                                      max_length=256)
    # 分析样本
    analyzing_data = models.CharField(max_length=256)
    # 插件内容
    content = models.TextField()
    # 查询条件
    search_tag = models.CharField(max_length=256)
    # 插件标签
    tag = models.CharField(max_length=125)
    post_data = models.TextField(default="")
    upload_time = models.DateTimeField(auto_now_add=True)


def get_file_path(instance, filename):
    return 'plug/%s/%s' % (instance.plug_type.p_type, filename)


class ScriptPlug(models.Model):
    """
    脚本插件类
    """
    id = models.AutoField(primary_key=True)
    script_file = models.FileField(upload_to=get_file_path)
    plug_type = models.ForeignKey('PlugType',
                                  on_delete=models.DO_NOTHING,
                                  related_name='script_plug')
    upload_time = models.DateTimeField(auto_now_add=True)


class PlugType(models.Model):
    """
    插件类型
    """
    id = models.AutoField(primary_key=True)
    p_type = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)
    num = models.IntegerField(default=0)
    content = models.CharField(max_length=256,
                               default="")
    name = models.CharField(max_length=256, default="")

