from django.db import models
from .crop import Crop
from .farm_type import FarmType
from .user import User


class Farmer(models.Model):
    farmer_name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=20, unique=True)
    farm_type = models.ForeignKey(FarmType, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.farmer_name
