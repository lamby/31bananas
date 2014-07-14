import json
import functools

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.contrib.messages.api import get_messages

class ajax(object):
    def __init__(self, required=True, login_required=False):
        self.required = required
        self.login_required = login_required

    def __call__(self, fn):
        @functools.wraps(fn)
        def wrapped(request, *args, **kwargs):
            if self.required and not request.is_ajax() \
                    and not request.user.is_superuser:
                return HttpResponseBadRequest()

            # @login_required returns a 30{1,2} redirect to some login page; we
            # want our Javascript applications to go down an "error" codepath
            # rather than try and parse the login page HTML, etc.
            if self.login_required and not request.user.is_authenticated():
                return HttpResponseBadRequest()

            response = fn(request, *args, **kwargs) or {}
            mimetype = 'text/html' if request.FILES else 'application/json'

            if isinstance(response, dict):
                return HttpResponse(
                    json.dumps(response),
                    content_type=mimetype,
                )

            return response
        return wrapped

def json_render(request, template=None, context=None, status='success', redirect_fallback=None):
    if not request.is_ajax() and redirect_fallback is not None:
        return redirect(redirect_fallback)

    result = context or {}

    if template is not None:
        request_context = RequestContext(request)

        # `context` not specified in RequestContext constructor since otherwise
        # the returned instance may have overriden keys, since the template
        # context processors take precedence over `context`. So, we have to
        # update after instantiation.
        request_context.update(context or {})

        result = {
            'html': render_to_string(template, request_context),
        }

    result.update({
        'status': status,
        '__messages__': [{
            'level': x.tags.split(' ')[0],
            'message': x.message,
        } for x in get_messages(request)],
    })

    return result
