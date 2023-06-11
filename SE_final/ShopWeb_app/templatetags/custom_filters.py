from django.template.defaultfilters import register
from datetime import timedelta

@register.filter(name='add_years')
def add_years(date, years):
    """
    這個過濾器會將日期格式的變數加上指定的年份
    """
    try:
        return date + timedelta(days=(years * 365))
    except TypeError:
        return None