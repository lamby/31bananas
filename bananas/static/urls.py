from django.conf.urls import patterns, url

urlpatterns = patterns('bananas.static.views',
    url(r'^$', 'landing',
        name='landing'),
)
