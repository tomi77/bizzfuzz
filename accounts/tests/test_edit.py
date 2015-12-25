from django.core.urlresolvers import reverse
from django.test import TestCase


class AccountsEditViewTestCase(TestCase):
    fixtures = ['users_views_testdata.yaml']

    def test_edit(self):
        url = reverse('edit', args=[1])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertTrue('user' in resp.context)
        self.assertEqual(resp.context['user'].pk, 1)
