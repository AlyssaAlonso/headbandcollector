from django.db import models
from django.urls import reverse

EVENTS = (
    ('R', 'Released'),
    ('I', 'In Stock'),
    ('O', 'Out of Stock')
)

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

class Status(models.Model):
  date = models.DateField()
  event = models.CharField(
    max_length=1,
    choices=EVENTS,
    default=EVENTS[1][0]
  )

  headband = models.ForeignKey(Headband, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.get_event_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']