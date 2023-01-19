"""
Test the landing page.
"""
from google.cloud import ndb

from django.urls import reverse

from bouncer.tests.base import DatastoreTestCase
from bouncer.models import Redirect


URL_LANDING = reverse('bouncer:landing')


class LandingPageTests(DatastoreTestCase):
    """Tests for the landing page."""

    def test_list_redirect_links(self):
        """Test link redirect links."""
        with self.ds_client.context():
            r1 = Redirect(
                name='Example 1 name',
                key=ndb.Key(Redirect, 'example-one'),
                destination_url='https://example.com/r1',
            )
            r1.put()
            r2 = Redirect(
                name='Example 2 name',
                key=ndb.Key(Redirect, 'example-two'),
                destination_url='https://example.com/r2',
            )
            r2.put()

        res = self.client.get(URL_LANDING)

        self.assertEqual(res.status_code, 200)
        for r in [r1, r2]:
            url = reverse('bouncer:redirect', kwargs={'slug': r.key.id()})
            self.assertContains(res, url)
            self.assertContains(res, r.name)
