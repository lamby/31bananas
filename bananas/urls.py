from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'', include('bananas.debug.urls', namespace='debug')),
    url(r'', include('bananas.reviews.urls', namespace='reviews')),
    url(r'', include('bananas.static.urls', namespace='static')),
)
