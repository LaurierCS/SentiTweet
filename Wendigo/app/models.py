from django.db import models

# Create your models here.
class TestModel(models.Model):
    name = models.CharField(blank=True, null=True)