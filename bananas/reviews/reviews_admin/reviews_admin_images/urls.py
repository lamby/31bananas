from django.conf.urls import patterns, url

urlpatterns = patterns('bananas.reviews.reviews_admin.reviews_admin_images.views',
    url(r'^xhr/admin/(?P<review_id>\d+)/images$', 'xhr_view',
        name='xhr-view'),
    url(r'^xhr/admin/(?P<review_id>\d+)/images/add$', 'add',
        name='add'),
    url(r'^xhr/admin/(?P<review_id>\d+)/images/add/url-u$', 'xhr_add_url',
        name='xhr-add-url'),
    url(r'^xhr/admin/(?P<review_id>\d+)/images/(?P<image_id>\d+)$', 'xhr_delete',
        name='xhr-delete'),
)
