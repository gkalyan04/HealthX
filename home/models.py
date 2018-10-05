from django.db import models

# Create your models here.

class Hospital(models.Model):

    name = models.TextField()
    address = models.TextField()
    street = models.TextField()
    landmark = models.TextField()
    locality = models.CharField(max_length=300)
    pincode = models.CharField(max_length=500)
    landline_number = models.CharField(max_length=500)
    latitude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)
    altitude = models.CharField(max_length=500)
    facility_name = models.CharField(max_length=264)
    state_name = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name