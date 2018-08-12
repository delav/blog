# coding:utf-8

from django import template
register = template.Library()


# 定义一个将日期中的月份转换为大写的过滤器
def upper(key):
    return ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'][key.month-1]


@register.filter
def assets(value):
    value.upper()
    return value


def num_to_mon(nums):
    # num_dict = {'01': "Jan", '02': "Feb", '03': "Mar", '04': "Apr", '05': "May", '06': "Jun", '07': "Jul",
    #             '08': "Aug", '09': "Sep", '10': "Oct", '11': "Nov", '12': "Dec"}
    return nums


# 注册过滤器
register.filter('upper', upper)
register.filter('assets', assets)
