from django.db import models

class Address(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=5)
    zipcode = models.CharField(max_length=10)
    msacode = models.CharField(max_length=10, default=None, blank=True, null=True)
    medianIncome = models.IntegerField(default=None, blank=True, null=True)
    isNacaApproved = models.BinaryField(editable=True, default=False, null=True, blank=True)
    geocode = models.JSONField(blank=True, null=True, default=None)




# Create your models here.
