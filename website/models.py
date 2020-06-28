from django.db import models
from django.urls import reverse
# Create your models here.


class FeedBack(models.Model):

    name = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    subject = models.CharField(max_length=400)
    message = models.TextField(max_length=10000)

    def __str__(self):
        return self.name
