from django.db import models
from city.models import City
from person.models import Person

# Create your models here.
class PersonalAddress(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)

    def __str__(self):
        return self.person.name + "(" + self.street_address + ")"