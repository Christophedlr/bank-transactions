from django import template
from copy import copy

register = template.Library()


# Adding a class attribute
@register.filter(is_safe=True)
def add_class(value, arg):
    classes = value.subwidgets[0].data['attrs']['class'] + ' ' + arg

    value = copy(value)
    return value.as_widget(attrs={'class': classes})
