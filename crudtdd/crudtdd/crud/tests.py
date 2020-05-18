from django.test import TestCase,Client
from django.urls import reverse,resolve
from .views import List,Get,Create,Update,Delete
from .models import list_Model
import json
class Test_List(TestCase):
    def setUp(self):
        self.client=Client()
        self.list=reverse('main')
    def test_list_url(self):
        self.assertEquals(resolve(self.list).func.view_class,List)
    def test_list_templete_status_code_and_Template_get(self):
        respanse = self.client.get(self.list)
        self.assertEquals(respanse.status_code,200)
        self.assertTemplateUsed(respanse, 'mian.html')
class Test_Create(TestCase):
    def setUp(self):
        self.client=Client()
        self.create=reverse('create')
    def test_create_url(self):
        self.assertEquals(resolve(self.create).func.view_class, Create)
    def test_list_templete_status_code_and_Template_get(self):
        respanse = self.client.get(self.create)
        self.assertEquals(respanse.status_code, 200)
        self.assertTemplateUsed(respanse, 'create.html')
    def test_update_templete_status_code_and_Template_post(self):
        data={
            'name': 'fqef'
        }
        respanse = self.client.post(self.create,data)
        self.model = list_Model.objects.get(id=1)
        self.assertEquals(respanse.status_code, 302)
class Test_Update(TestCase):
    def setUp(self):
        self.client=Client()
        self.update=reverse('update', kwargs={"id":1})
    def test_update_url(self):
        self.assertEquals(resolve(self.update).func.view_class, Update)
    def test_update_templete_status_code_and_Template_get(self):
        list_Model.objects.create(name='dqd')
        respanse = self.client.get(self.update)
        self.assertEquals(respanse.status_code, 200)
        self.assertTemplateUsed(respanse, 'create.html')
    def test_update_templete_status_code_and_Template_post(self):
        list_Model.objects.create(name='dqd')
        data={
            'name': 'fqef'
        }
        respanse = self.client.post(self.update,data)
        self.model = list_Model.objects.get(id=1)
        self.assertEquals(respanse.status_code, 302)
class Test_Delete:
    def setUp(self):
        self.client=Client()
        self.delete=reverse('delete', kwargs={"id":1})
    def test_delete_url(self):
        self.assertEquals(resolve(self.delete).func.view_class, Delete)
    def test_delete_action(self):
        list_Model.objects.create(name='dqd')
        self.client.delete(self.delete,json.dumps({
            'id':1
        }))
        self.assertEquals(len(list_Model.objects.all()),0)
class TestModel_list_Model(TestCase):
    def setUp(self) -> None:
        list_Model.objects.create(name='dqd')
        self.model=list_Model.objects.get(id=1)
    def test_model_get_url(self):
        self.assertEquals(self.model.get_url,'/get/1/')
    def test_model_get_update_url(self):
        self.assertEquals(self.model.update_url,'/update/1/')
    def test_model_get_delete_url(self):
        self.assertEquals(self.model.delete_url, '/delete/1/')





