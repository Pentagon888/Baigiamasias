



from django.db import models
from django.contrib.auth.models import User

class RepairCategory(models.Model):
    name = models.CharField(max_length=50)



    def __str__(self):
        return self.name

class AutoService(models.Model):
    name = models.CharField(verbose_name="Vardas",max_length=100)
    category = models.ManyToManyField(RepairCategory,verbose_name="Kategorija", blank=True)
    location_lat = models.FloatField(verbose_name="Lokacijos Platuma")
    location_lon = models.FloatField(verbose_name="Lokacijos Ilguma")
    address = models.CharField(verbose_name="adresas", max_length=200)
    phone_number = models.CharField(verbose_name="Telefono numeris", max_length=20)
    working_hours = models.CharField( verbose_name=" Darbo valandosmax",max_length=100)

    def __str__(self):
        return self.name
