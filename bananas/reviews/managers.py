from django.db import models

class ReviewManager(models.Manager):
    def public(self):
        return self.filter(published=True)
