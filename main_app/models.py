from django.db import models
from django.urls import reverse

# Create your models here.
class Headband(models.Model):
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'headband_id': self.id})