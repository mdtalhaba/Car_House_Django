from django.db import models
from brand.models import Brand

class Car(models.Model) :
    title = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to='car/media/uploads/', blank=True, null=True)

    def __str__(self) :
        return self.title



