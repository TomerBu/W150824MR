from django import template

register = template.Library()

# this function accepts a list/tuple
# and returns space joined str
# ["django", "pyhton"] => "django python"

@register.filter
def join_space(value):
    if isinstance(value, (list, tuple)):
        return " ".join(value)
    return value

# {% tags|join_space %}