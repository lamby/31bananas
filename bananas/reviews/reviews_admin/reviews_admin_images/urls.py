from django.conf.urls import patterns, url

urlpatterns = patterns('bananas.reviews.reviews_admin.reviews_admin_images.views',
    url(r'^xhr/admin/(?P<review_id>\d+)/images$', 'xhr_view',
        name='xhr-view'),
    url(r'^xhr/admin/(?P<review_id>\d+)/images/add$', 'add',
        name='add'),
    url(r'^xhr/admin/(?P<review_id>\d+)/images/add/url$', 'xhr_add_url',
        name='xhr-add-url'),
    url(r'^xhr/admin/(?P<review_id>\d+)/images/(?P<image_id>\d+)/delete$', 'xhr_delete',
        name='xhr-delete'),
    url(r'^xhr/admin/(?P<review_id>\d+)/images/(?P<image_id>\d+)/move-right$', 'xhr_move_right',
        name='xhr-move-right'),
)
