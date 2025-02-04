from django.db import models
from django.urls import reverse
class list_Model(models.Model):
    name=models.CharField(max_length=150)
    @property
    def delete_url(self):
        return reverse("crud:delete", kwargs={"id": self.id})
    @property
    def get_url(self):
        return reverse("crud:Get", kwargs={"id":self.id})
    @property
    def update_url(self):
        return reverse("crud:update", kwargs={"id":self.id})
    def __str__(self):
        return  self.name