from django.test import SimpleTestCase
from djnag.urls import reverse,resolve
from .views import List
class TestsUrls(SimpleTestCase):
    def test_list(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class,List)


