import os
import scss

from django.template import Template, Context

def render_file(fullpath):
    with open(fullpath) as f:
        contents = f.read()

    extension = os.path.splitext(fullpath)[1][1:].lower()

    # SASS CSS
    if extension == 'scss':
        contents = Template(contents).render(Context({}))

        contents = scss.Scss(scss_opts={
            'compress': False,
        }).compile(contents)

    return contents
