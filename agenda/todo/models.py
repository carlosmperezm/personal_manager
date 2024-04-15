from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length=100)
    descryption = models.TextField(blank=True,null=True)
    date = models.DateField(default=date.today)
    estimed_end = models.DateField(blank=True,null=True)
    priority = models.IntegerField(default=3)

    def __str__(self):
        return self.title
