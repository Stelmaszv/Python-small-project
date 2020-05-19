from django.db import models

class List(models.Model):
    name = models.CharField(max_length=50)
