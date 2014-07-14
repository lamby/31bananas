from django.core.exceptions import ObjectDoesNotExist
from django.contrib.syndication.views import Feed

from .models import Post

NUM_ITEMS = 10

class AllItems(Feed):
    link = '/'
    title = "lamby"
    title_template = 'blog/rss_title.html'
    description_template = 'blog/rss.html'

    def items(self):
        return Post.objects.for_feed()[:NUM_ITEMS]

    def item_pubdate(self, obj):
        return obj.published
