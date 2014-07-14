import os
import stat
import mimetypes

from django.conf import settings
from django.http import HttpResponse, HttpResponseNotModified, Http404
from django.shortcuts import render, render_to_response
from django.utils.http import http_date
from django.views.static import directory_index, was_modified_since

from .utils import render_file

def media(request, path):
    fullpath = os.path.join(settings.STATIC_MEDIA_ROOT, path)
    mimetype = mimetypes.guess_type(fullpath)[0] or 'application/octet-stream'

    # Rendering directory listing
    if os.path.isdir(fullpath):
        return directory_index(path, fullpath)

    # Render single file
    if not os.path.isdir('%s.d' % fullpath):
        try:
            modified = os.stat(fullpath)[stat.ST_MTIME]
        except OSError:
            raise Http404()

        if not was_modified_since(
            request.META.get('HTTP_IF_MODIFIED_SINCE'),
            modified,
        ):
            return HttpResponseNotModified(content_type=mimetype)

        contents = render_file(fullpath)
        response = HttpResponse(contents, content_type=mimetype)
        response['Last-Modified'] = http_date(modified)
        response['Content-Length'] = len(contents)

        return response

    # Render .d directory

    latest = -1
    filenames = []

    for root, _, files in os.walk('%s.d' % fullpath, followlinks=True):
        for filename in [os.path.join(root, x) for x in files]:
            if filename.endswith('~'):
                continue
            filenames.append(filename)
            latest = max(latest, os.stat(filename)[stat.ST_MTIME])

    if not was_modified_since(
        request.META.get('HTTP_IF_MODIFIED_SINCE'),
        latest,
    ):
        return HttpResponseNotModified(content_type=mimetype)

    contents = ""
    for filename in sorted(filenames):
        contents += render_file(filename)

    response = HttpResponse(contents, content_type=mimetype)
    response['Last-Modified'] = http_date(latest)
    response['Content-Length'] = len(contents)

    return response

def http500(request):
    # Django does not render this page with a RequestContext
    return render_to_response('500.html')

def http404(request):
    # Django *does* render this page with a RequestContext.
    return render(request, '404.html')
