from django.conf import settings
from django.conf.urls import patterns, url

urlpatterns = []

if settings.DEBUG:
    urlpatterns += patterns('bananas.debug.views',
        url(r'^media/(?P<path>.*)$', 'media'),
        url(r'^404$', 'http404',
            name='http-404'),
        url(r'^500$', 'http500',
            name='http-500'),
    )

    urlpatterns += patterns('django.views.static',
        url(r'^storage/(?P<path>.*)$', 'serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
