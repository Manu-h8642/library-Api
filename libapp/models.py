from django.db import models

# Create your models here.
class bdb(models.Model):
    bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=100)
    aname = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()