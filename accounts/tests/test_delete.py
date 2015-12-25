from django.core.urlresolvers import reverse
from django.test import TestCase


class AccountsDeleteViewTestCase(TestCase):
    fixtures = ['users_views_testdata.yaml']

    def test_delete_non_existent_user(self):
        url = reverse('del', args=[99])
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)
        self.assertTrue('alert' in resp.context)
        self.assertIsNotNone(resp.context['alert'])
