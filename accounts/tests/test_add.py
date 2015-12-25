from django.core.urlresolvers import reverse
from django.test import TestCase


class AccountsAddViewTestCase(TestCase):
    fixtures = ['users_views_testdata.yaml']

    def test_add(self):
        url = reverse('add')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
