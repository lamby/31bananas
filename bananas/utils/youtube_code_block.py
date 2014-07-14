# http://countergram.com/youtube-in-rst

from docutils import nodes
from docutils.parsers.rst import directives

CODE = """\
<p class="object">
    <object
        type="application/x-shockwave-flash"
        width="%(width)s"
        height="%(height)s"
        class="youtube-embed"
        data="//www.youtube.com/v/%(yid)s?start=%(start)s"
    >
        <param name="movie" value="//www.youtube.com/v/%(yid)s?start=%(start)s"></param>
        <param name="wmode" value="transparent"></param>
        %(extra)s
    </object>
</p>
"""

PARAM = """\n    <param name="%s" value="%s"></param>"""

def youtube(name, args, options, content, lineno, contentOffset, blockText, state, stateMachine):
    """
    Restructured text extension for inserting youtube embedded videos.
    """

    if len(content) == 0:
        return

    string_vars = {
        'yid': content[0],
        'start': 0,
        'extra': '',
        'width': 600,
        'height': 400,
    }

    extra_args = dict(
        x.strip().split(': ', 1) for x in content[1:]
    )

    for x in ('width', 'height', 'start'):
        if x in extra_args:
            string_vars[x] = extra_args.pop(x)

    if extra_args:
        params = [PARAM % (key, extra_args[key]) for key in extra_args]
        string_vars['extra'] = "".join(params)

    return [nodes.raw('', CODE % (string_vars), format='html')]

youtube.content = True
directives.register_directive('youtube', youtube)
