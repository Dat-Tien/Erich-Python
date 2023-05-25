from django.db import models
from topic1.models import Topics
# Create your models here.
class Blog(models.Model):
    blogName = models.CharField(max_length=200)
    topics = models.ManyToManyField(Topics)
    
    def __str__(self):
        return self.blogName