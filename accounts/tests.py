from django.core.urlresolvers import reverse
from django.test import TestCase


class AccountsViewsTestCase(TestCase):
    fixtures = ['users_views_testdata.yaml']

    def test_index(self):
        url = reverse('index')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertTrue('users' in resp.context)
        self.assertEqual([user.pk for user in resp.context['users']], [1, 2, 3, 4])

    def test_details(self):
        url = reverse('view', args=[1])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertTrue('user' in resp.context)
        self.assertEqual(resp.context['user'].pk, 1)

    def test_edit(self):
        url = reverse('edit', args=[1])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertTrue('user' in resp.context)
        self.assertEqual(resp.context['user'].pk, 1)

    def test_add(self):
        url = reverse('add')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_delete_non_existent_user(self):
        url = reverse('del', args=[99])
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)
        self.assertTrue('alert' in resp.context)
        self.assertIsNotNone(resp.context['alert'])
