from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name