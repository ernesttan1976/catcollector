from django.db import models

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    image = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.name