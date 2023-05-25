from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import  PersonalAddress
from .serializers import PersonAddressSerializer
from person.models import Person
from city.models import City
from interest.models import Interest


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful.'})
        else:
            return Response({'message': 'Invalid username or password.'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logout successful.'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def personalAddress_create(request):
    personalAddressData = request.data
    newPersonAddress = PersonalAddress.objects.create(
        person=Person.objects.get(id=personalAddressData["person"]),
        city=City.objects.get(id=personalAddressData["city"]),
        street_address= personalAddressData["street_address"])
    newPersonAddress.save()
    personSerializer = PersonAddressSerializer(newPersonAddress)
    return Response(personSerializer.data)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def personalAddress_update(request, id):
    updateData = request.data
    instance = get_object_or_404(PersonalAddress, pk=id) #Application.objects.get(pk=id)
    personSerializer = PersonAddressSerializer(instance, data=updateData)
    personSerializer.is_valid(raise_exception=True)
    personSerializer.save()
    # print(instance.person.interests)
    # interests = []
    # for interestId in instance.person.interests:
    #     print(interestId)
    #     interest_obj = get_object_or_404(Interest, pk=interestId) 
    #     interests.append(interest_obj)
    # instance.interests.set(interests)
    return Response(personSerializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def personalAddress_get(request):
    personalAddress = PersonalAddress.objects.all()
    personalAddressSerializer = PersonAddressSerializer(personalAddress, many=True) # many=True means 
    return JsonResponse(personalAddressSerializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def personalAddress_detail(request, id):
    personAddr = get_object_or_404(PersonalAddress, pk=id)
    personAddrSerializer = PersonAddressSerializer(personAddr) # many=True means 
    return JsonResponse(personAddrSerializer.data, safe=False)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def personalAddress_delete(request, id):
    instance = get_object_or_404(PersonalAddress, pk=id)
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)