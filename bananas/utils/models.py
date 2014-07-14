from django import template

from . import youtube_code_block

template.add_to_builtins('bananas.utils.templatetags.fonts')
template.add_to_builtins('bananas.utils.templatetags.media')
template.add_to_builtins('bananas.utils.templatetags.python')
template.add_to_builtins('bananas.utils.templatetags.text')
template.add_to_builtins('cache_toolbox.templatetags.cache_toolbox')
template.add_to_builtins('django_autologin.templatetags.django_autologin')

youtube_code_block = youtube_code_block # appease linters
