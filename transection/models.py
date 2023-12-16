from django.db import models
from django.contrib.auth.models import User

class Transection(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.CharField(max_length=50)
    quantity = models.IntegerField()

