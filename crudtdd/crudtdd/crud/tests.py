from django.test import TestCase,Client
from django.urls import reverse,resolve
from .views import List,Get
from .models import list_Model
class TestTemplate(TestCase):
    def setUp(self):
        self.client=Client()
        self.list=reverse('main')
        self.get=reverse('Get', kwargs={"id":1})
        list_Model.objects.create(name='dqd')
    def test_list(self):
        self.assertEquals(resolve(self.list).func.view_class,List)
    def test_get_url(self):
        self.assertEquals(resolve(self.get).func.view_class,Get)
    def test_list_templete(self):
        respanse = self.client.get(self.list)
        self.assertEquals(respanse.status_code,200)
        self.assertTemplateUsed(respanse, 'mian.html')
    def test_get_status_code(self):
        respanse = self.client.get(self.get)
        self.assertEquals(respanse.status_code, 200)
    def test_list_templete(self):
        respanse = self.client.get(self.get)
        self.assertTemplateUsed(respanse, 'get.html')





