from django.db import models
from django.urls import reverse
from datetime import date

EVENTS = (
    ('R', 'Released'),
    ('I', 'In Stock'),
    ('O', 'Out of Stock')
)

# Create your models here.
class Accessory(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})

class Headband(models.Model):
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'headband_id': self.id})
    
    def updated_today(self):
      return self.status_set.filter(date=date.today()).count() >= 1


class Status(models.Model):
  date = models.DateField()
  event = models.CharField(
    max_length=1,
    choices=EVENTS,
    default=EVENTS[1][0]
  )

  headband = models.ForeignKey(
    Headband,
    on_delete=models.CASCADE
  )

  headband = models.ForeignKey(Headband, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.get_event_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']