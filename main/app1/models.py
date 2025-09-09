from django.db import models

# Create your models here.

class Tour(models.Model):
    origin_country = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
            return (f"ID:{self.id} : from {self.origin_country} to "
                    f"{self.destination_country} , for a duration of {self.duration} "
                    f"days at the price of {self.price} INR ")