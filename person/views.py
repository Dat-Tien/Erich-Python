from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status

from .models import  Person
from .serializers import PersonSerializer
from interest.models import Interest
from interest.serializers import InterestSerializer



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request, *args, **kwargs):
    person = request.data # get data from resquest.
    newPerson = Person.objects.create(
        name=person["name"], mobile=person["mobile"])
    newPerson.save()
    for dataAdd in person["interests"]:
        interest_obj = get_object_or_404(Interest, pk=dataAdd) 
        newPerson.interests.add(interest_obj)
    
    personSerializer = PersonSerializer(newPerson)
    # personSerializer = PersonSerializer(data=person)
    # personSerializer.is_valid(raise_exception=True)
    # personSerializer.save()
    return Response(personSerializer.data)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, id):
    person = request.data
    instance = get_object_or_404(Person, pk=id) #Application.objects.get(pk=id)
    personSerializer = PersonSerializer(instance, data=person)
    personSerializer.is_valid(raise_exception=True)
    personSerializer.save()
    
    interests = []
    for interestId in person["interests"]:
        print(interestId)
        interest_obj = get_object_or_404(Interest, pk=interestId) 
        interests.append(interest_obj)
    instance.interests.set(interests)
    return Response(personSerializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request):
    interest = InterestSerializer(read_only=True, many=True)
    person = Person.objects.all()
    personSerializer = PersonSerializer(person, many=True) # many=True means 
    return JsonResponse(personSerializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request, id):
    person = get_object_or_404(Person, pk=id)
    personSerializer = PersonSerializer(person) # many=True means 
    return JsonResponse(personSerializer.data, safe=False)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    instance = get_object_or_404(Person, pk=id)
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)