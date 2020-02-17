from django.template import Library
from django import template
from django.utils.safestring import mark_safe
from re import sub

# 将注册类实例化为register对象
register = Library()


# 使用装饰器注册
@register.filter
def replacePath(path):
    # 去路径前缀
    return sub('.*/', '', path)


@register.filter
def replaceExt(path):
    # 去文件后缀
    return sub('\..*', '', path)

@register.filter
def getExt(path):
    # 取文件后缀（扩展名）
    return sub('.*\.', '', path)