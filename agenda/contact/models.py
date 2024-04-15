from django.db import models
from datetime import date 

class Contact(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(blank=True,null=True,max_length=50)
    mobile = models.CharField(max_length=12,default=0)
    phone = models.CharField(blank=True,null=True,max_length=12)
    email = models.EmailField(max_length=100)
    company = models.CharField(blank=True,null=True,max_length=50)
    date = models.DateField(default=date.today)
    notes = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
