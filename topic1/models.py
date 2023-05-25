from django.db import models

# Create your models here.

class Topics(models.Model):
    Author = models.CharField(max_length=50)
    TopicName = models.CharField(max_length=200)
    DateOfPublish = models.DateField(auto_now=True)
    Contact = models.CharField(max_length=14)

    def __str__(self):
        return self.Author + self.TopicName

