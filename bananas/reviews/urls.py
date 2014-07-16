from django.conf.urls import patterns, url, include

urlpatterns = patterns('bananas.reviews.views',
    url(r'', include('bananas.reviews.reviews_admin.urls', namespace='admin')),

    url(r'^day-(?P<day>\d+)-(?P<slug>[^\/]*)$', 'view',
        name='view'),
)
