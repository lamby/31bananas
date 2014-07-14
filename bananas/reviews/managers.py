import datetime

from django.db import models

class ReviewManager(models.Manager):
    def public(self):
        return self.filter(date__gte=datetime.datetime.today())
