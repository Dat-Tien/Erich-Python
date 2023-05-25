from rest_framework import serializers
from .models import PersonalAddress
from person.serializers import PersonSerializer
from city.serializers import CitySerializer

class PersonAddressSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    city = CitySerializer()
    class Meta:
        model = PersonalAddress
        fields = ['id','street_address', 'person', 'city']
        # depth = 1