from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe = True)
def replace_n(value):
    return value.replace('\n', '<br />')
