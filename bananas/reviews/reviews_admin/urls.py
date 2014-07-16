from django.conf.urls import patterns, url, include

urlpatterns = patterns('bananas.reviews.reviews_admin.views',
    url(r'', include('bananas.reviews.reviews_admin.reviews_admin_images.urls', namespace='images')),

    url(r'^admin/login$', 'login',
        name='login'), # settings.LOGIN_URL
    url(r'^admin$', 'index',
        name='index'),

    url(r'^admin/edit/(?P<review_id>\d+)$', 'edit',
        name='edit'),
    url(r'^xhr/admin/save/(?P<review_id>\d+)$', 'xhr_edit',
        name='xhr-edit'),
)
