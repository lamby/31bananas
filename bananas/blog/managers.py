import datetime

from django.db import models

class PostManager(models.Manager):
    def published(self):
        return self.filter(published__lte=datetime.datetime.utcnow())

    def for_feed(self):
        return self.published().filter(
            published__gt=datetime.datetime(2012, 12, 14, 0, 0),
        )

class CommentManager(models.Manager):
    def moderated(self):
        return self.filter(is_moderated=True)

    def unmoderated(self):
        return self.filter(is_moderated=False)

class TagManager(models.Manager):
    def planets(self):
        return self.filter(planet=True)

    def tags(self):
        return self.filter(planet=False)
