from django.db import models 

class getempdetails(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email  = models.CharField(max_length=100)