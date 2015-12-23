from django.test import TestCase


class AccountsViewsTestCase(TestCase):
    fixtures = ['users_views_testdata.yaml']

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('users' in resp.context)
        self.assertEqual([user.pk for user in resp.context['users']], [1, 2, 3])

    def test_details(self):
        resp = self.client.get('/view/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('user' in resp.context)
        self.assertEqual(resp.context['user'].pk, 1)

    def test_edit(self):
        resp = self.client.get('/edit/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('user' in resp.context)
        self.assertEqual(resp.context['user'].pk, 1)
