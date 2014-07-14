import datetime

from django_yadt import YADTImageField

from django.db import models

from .managers import PostManager, CommentManager, TagManager

class Post(models.Model):
    title = models.CharField(max_length=250, blank=True)
    content = models.TextField(blank=True)

    slug = models.SlugField(
        max_length=70,
        null=True,
        blank=True,
        unique=True,
        default=None,
    )

    cover = YADTImageField(variants={
        'xs': {
            'width': 768,
            'height': 768,
            'format': 'jpeg',
            'kwargs': {
                'quality': 70,
            },
        },
        'sm': {
            'width': 992,
            'height': 992,
            'format': 'jpeg',
            'kwargs': {
                'quality': 70,
            },
        },
        'md': {
            'width': 1200,
            'height': 1200,
            'format': 'jpeg',
            'kwargs': {
                'quality': 75,
            },
        },
        'lg': {
            'width': 1800,
            'height': 1800,
            'format': 'jpeg',
            'kwargs': {
                'quality': 80,
            },
        },
    }, cachebust=True)

    has_cover = models.BooleanField(default=False)

    created = models.DateTimeField(default=datetime.datetime.utcnow)
    published = models.DateTimeField(default=None, null=True, blank=True)

    objects = PostManager()

    class Meta:
        ordering = ('-published',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'blog:post', (self.slug,)
