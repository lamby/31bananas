from django import template

register = template.Library()

@register.filter('range')
def range_(val):
    return range(val)

@register.filter
def getitem(obj, att):
    if obj:
        return obj.get(att, None)
