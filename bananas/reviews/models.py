import datetime

from django_yadt import YADTImageField

from django.db import models
from django.utils.text import slugify

from .managers import ReviewManager

YEAR, MONTH = 2014, 8

class Review(models.Model):
    title = models.CharField(max_length=250, blank=True)

    source = models.CharField(max_length=250, blank=True)
    price = models.CharField(max_length=250, blank=True)
    score = models.IntegerField(default=3)

    content = models.TextField(blank=True)

    nutrition = models.CharField(max_length=250, blank=True)
    nutrition_serving = models.CharField(max_length=250, blank=True)

    date = models.DateField(unique=True)
    published = models.BooleanField(default=False)

    created = models.DateTimeField(default=datetime.datetime.utcnow)

    objects = ReviewManager()

    class Meta:
        ordering = ('date',)

    def __unicode__(self):
        return u"%s" % self.title

    @models.permalink
    def get_absolute_url(self):
        return 'reviews:view', (self.date.day, self.slug())

    def slug(self):
        return slugify(self.title)

class Image(models.Model):
    review = models.ForeignKey('reviews.Review', related_name='images')

    image = YADTImageField(variants={
        'cover': {
            'crop': True,
            'width': 1000,
            'height': 500,
            'format': 'jpeg',
        },
        'thumbnail': {
            'crop': True,
            'width': 200,
            'height': 150,
            'format': 'jpeg',
        },
    }, cachebust=True)

    order = models.IntegerField()

    class Meta:
        ordering = ('order',)
        unique_together = (
            ('review', 'order'),
        )
