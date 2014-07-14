from django import template

register = template.Library()

@register.filter
def getitem(obj, att):
    if obj:
        return obj.get(att, None)
