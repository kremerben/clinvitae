from django.template import Library

register = Library()


@register.filter(is_safe=True)
def get(value, arg):
    """
    Helps return values when the objects keys have a space in the string
    ex: obj['two words']
    """
    return value.get(arg, '')
