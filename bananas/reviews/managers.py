import datetime

from django.db import models

# 10AM BST
PUBLISH_AT = datetime.time(9, 15)

class ReviewManager(models.Manager):
    def public(self):
        epoch = datetime.datetime.utcnow()

        if epoch.time() < PUBLISH_AT:
            epoch -= datetime.timedelta(days=1)

        return self.filter(
            date__lte=epoch.date(),
            published=True,
        )
