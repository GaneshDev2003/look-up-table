from django.db import models

# Create your models here.
class EntriesModel(models.Model):
    name = models.CharField(default='', max_length=100)
    age = models.IntegerField(default='0')
    country = models.CharField(default='',max_length=50)
    company = models.CharField(default='',max_length=50)
    branch = models.CharField(default='',max_length=20)
    batch = models.CharField(default='',max_length=20)