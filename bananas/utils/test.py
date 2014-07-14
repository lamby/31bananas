from django.db import models
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class TestCase(TestCase):
    def make_user(self, username, email=None):
        if email is None:
            email = '%s@example.com' % username

        return User.objects.create_user(username, email, 'password')

    def assertStatusCode(self, status_code, fn, urlconf, *args, **kwargs):
        if kwargs.pop('login', False):
            self.client.login(username='testuser', password='password')

        response = fn(reverse(urlconf, args=args, kwargs=kwargs))

        self.assertEqual(response.status_code, status_code, response)
