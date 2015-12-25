from django.core.urlresolvers import reverse
from django.test import TestCase


class AccountsIndexViewTestCase(TestCase):
    fixtures = ['users_views_testdata.yaml']

    def test_index(self):
        url = reverse('index')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertTrue('users' in resp.context)
        self.assertEqual([user.pk for user in resp.context['users']], [1, 2, 3, 4])
