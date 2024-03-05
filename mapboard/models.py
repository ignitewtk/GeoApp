from django.db import models

# Create your models here.

class Position(models.Model):
    position_name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    modified_date = models.DateTimeField("Date Modified", auto_now=True)

    def _str__(self):
        return f"Longitude: {self.longitude}, Latitude: {self.latitude}"