from django import template

register = template.Library()

@register.filter()
def cell_color(value):
    if value == '':
        return 'white'

    value = float(value)
    if value < 0:
        return 'green'

    if value >= 1 and value < 2:
        return 'IndianRed'

    if value >= 2 and value < 5:
        return 'Crimson'

    if value >= 5:
        return 'DarkRed'

    return 'white'