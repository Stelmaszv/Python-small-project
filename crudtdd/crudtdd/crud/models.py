from django.db import models
from django.urls import reverse
class list_Model(models.Model):
    name=models.CharField(max_length=150)
    @property
    def model_url(self):
        return reverse("Get", kwargs={"id":self.id})
    def __str__(self):
        return  self.name