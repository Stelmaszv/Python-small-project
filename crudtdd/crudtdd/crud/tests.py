from django.test import TestCase,Client
from django.urls import reverse,resolve
from .views import List,Get,Create
from .models import list_Model
class TestTemplate(TestCase):
    def setUp(self):
        self.client=Client()
        self.list=reverse('main')
        self.get=reverse('Get', kwargs={"id":1})
        self.create=reverse('create')
    def test_create(self):
        self.assertEquals(resolve(self.create).func.view_class, Create)
    def test_list(self):
        self.assertEquals(resolve(self.list).func.view_class,List)
    def test_get_url(self):
        self.assertEquals(resolve(self.get).func.view_class,Get)
    def test_list_templete(self):
        respanse = self.client.get(self.list)
        self.assertEquals(respanse.status_code,200)
        self.assertTemplateUsed(respanse, 'mian.html')
    def test_create_templete_status_code_and_Template_get(self):
        respanse = self.client.get(self.create)
        self.assertEquals(respanse.status_code,200)
        self.assertTemplateUsed(respanse, 'create.html')
    def test_create_templete_status_code_and_Template_post(self):
        respanse = self.client.post(self.create,{
            'name':'fqef'
        })
        self.assertEquals(respanse.status_code,302)
        self.assertEquals(len(list_Model.objects.all()),1)
    def test_get_status_code_and_Template(self):
        list_Model.objects.create(name='dqd')
        respanse = self.client.get(self.get)
        self.assertTemplateUsed(respanse, 'get.html')
        self.assertEquals(respanse.status_code, 200)
class TestModel_list_Model(TestCase):
    def setUp(self) -> None:
        list_Model.objects.create(name='dqd')
        self.model=list_Model.objects.get(id=1)
    def test_model_get_url(self):
        self.assertEquals(self.modelur(),'get/1/')





