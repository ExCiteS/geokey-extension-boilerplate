from django.test import TestCase
from django.core.urlresolvers import reverse, resolve

from ..views import IndexPage


class UrlsTest(TestCase):

    def test_index_page_reverse(self):
        reversed = reverse('geokey_extension:index')
        self.assertEqual(reversed, '/admin/awesome-extension/')

    def test_index_page_resolve(self):
        resolved = resolve('/admin/awesome-extension/')
        self.assertEqual(resolved.func.__name__, IndexPage.__name__)
