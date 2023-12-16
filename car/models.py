from django.db import models
from brand.models import Brand


class Car(models.Model) :
    title = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='car/media/uploads/', blank=True, null=True)

    def __str__(self) :
        return self.title
    
class Comment(models.Model) :
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"Comment by {self.name}"





