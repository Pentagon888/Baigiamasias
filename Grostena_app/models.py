



from django.db import models
from django.contrib.auth.models import User

class RepairCategory(models.Model):
    name = models.CharField(max_length=50)



    def __str__(self):
        return self.name

class AutoService(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(RepairCategory, blank=True)
    location_lat = models.FloatField()
    location_lon = models.FloatField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    working_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.name

