from django.db import models

class zipcode(models.Model):
    znum = models.IntegerField(unique=True)
    wcode = models.CharField(max_length=100)
    
    def __str__(self):
        self.wcode
# Create your models here.

class Alert(models.Model):
    headline = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    ref_url = models.ForeignKey(zipcode, on_delete=models.SET_NULL, null=True)
    ends = models.CharField(max_length=50)
    instruct = models.CharField(max_length=400)
    severity = models.CharField(max_length=50)
    event = models.CharField(max_length=50)