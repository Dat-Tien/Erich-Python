from django.db import models
from interest.models import Interest

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return self.name