from django import template
from django.utils.html import escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()

TEMPLATE = """
     <span class="visible-xs-inline">%s %s</span><span class="hidden-xs">%s&nbsp;%s</span>
"""

@register.filter
def widont(val):
    val = escape(force_unicode(val))

    try:
        head, tail = val.rsplit(' ', 1)

        val = TEMPLATE.strip() % (head, tail, head, tail)
    except ValueError:
        pass

    return mark_safe(val)

@register.filter
def split(val, sep='\n'):
    return [x.strip() for x in val.split(sep)]
