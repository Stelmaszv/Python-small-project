from django.test import SimpleTestCase,TestCase
from django.urls import reverse,resolve
from .views import List
class TestsUrls(SimpleTestCase):
    def test_list(self):
        url = reverse('main')
        self.assertEquals(resolve(url).func.view_class,List)
class TestTemplate(TestCase):
    def test_list(self):
        url = reverse('main')
        respanse = self.client.get(url)
        self.assertEquals(respanse.status_code,200)
        self.assertTemplateUsed(respanse, 'mian.html')





