from django import template
register = template.Library()

@register.filter(name='rusify')
def change(value):
    return value.replace('w', 'v')
