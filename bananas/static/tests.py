from bananas.utils.test import TestCase

class SmokeTests(TestCase):
    def test_landing(self):
        self.assertStatusCode(200, self.client.get, 'static:landing')
