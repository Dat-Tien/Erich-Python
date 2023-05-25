from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status

from .models import  City
from .serializers import CitySerializer



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    city = request.data # get data from resquest.
    citySerializer = CitySerializer(data=city)
    citySerializer.is_valid(raise_exception=True) # auto return 400
    citySerializer.save()
    return Response(citySerializer.data)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, id):
    instance = get_object_or_404(City, pk=id) #Application.objects.get(pk=id)
    city = request.data
    citySerializer = CitySerializer(instance, data=city)
    citySerializer.is_valid(raise_exception=True)
    citySerializer.save()
    return Response(citySerializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request):
    city = City.objects.all()
    citySerializer = CitySerializer(city, many=True) # many=True means 
    return JsonResponse(citySerializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request, id):
    city = get_object_or_404(City, pk=id)
    citySerializer = CitySerializer(city) # many=True means 
    return JsonResponse(citySerializer.data, safe=False)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    instance = get_object_or_404(City, pk=id)
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)