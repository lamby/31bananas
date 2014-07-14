from django.conf.urls import patterns, url, include

from . import feeds

urlpatterns = patterns('bananas.blog.views',
    url(r'', include('bananas.blog.blog_admin.urls', namespace='admin')),

    url(r'^(?P<number>\d+)-(?P<slug>[^\/]*)$', 'view',
        name='view'),
)

urlpatterns += patterns('bananas.blog.feeds',
    url(r'^feed/$', feeds.AllItems(),
        name='feed'),
)
