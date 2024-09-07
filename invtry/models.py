from django.db import models

# Create your models here.

class Drug(models.Model):
    drugid = models.IntegerField()
    name = models.CharField(max_length=256)
    manufacturer = models.CharField(max_length=512)
    drugtype = models.CharField(max_length=128)
    quantity = models.IntegerField()
    expirydate = models.DateField()
    description = models.TextField()
    batchno = models.CharField(max_length=126)
