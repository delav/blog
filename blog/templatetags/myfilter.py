# coding:utf-8

from django import template
register = template.Library()


# 定义一个将日期中的月份转换为大写的过滤器
def upper(key):
    return ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'][key.month-1]
# 注册过滤器
register.filter('upper', upper)


@register.filter
def assets(value):
    value.upper()
    return value
# register.filter('assets', assets)

