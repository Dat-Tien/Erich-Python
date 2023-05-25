from rest_framework import serializers
from .models import Person
from interest.serializers import InterestSerializer

class PersonSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(read_only=True, many=True)
    class Meta:
        model = Person
        fields = ('id','name','mobile', 'interests')