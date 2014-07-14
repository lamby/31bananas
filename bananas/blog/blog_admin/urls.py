from django.conf.urls import patterns, url

urlpatterns = patterns('bananas.blog.blog_admin.views',
    url(r'^login$', 'login',
        name='login'),
    url(r'^admin$', 'index',
        name='index'),

    url(r'^admin/add$', 'add',
        name='add'),
    url(r'^admin/edit/(?P<post_id>\d+)$', 'edit',
        name='edit'),
    url(r'^admin/delete/(?P<post_id>\d+)$', 'delete',
        name='delete'),

    url(r'^xhr/admin/save/(?P<post_id>\d+)$', 'xhr_edit',
        name='xhr-edit'),
    url(r'^xhr/admin/cover/(?P<post_id>\d+)$', 'xhr_cover_url',
        name='xhr-cover-url'),

    url(r'^admin/comments/moderate/(?P<comment_id>\d+)$', 'moderate_comment',
        name='moderate-comment'),
)
