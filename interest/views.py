from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status

from .models import  Interest
from .serializers import InterestSerializer



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    interest = request.data # get data from resquest.
    interestSerializer = InterestSerializer(data=interest)
    interestSerializer.is_valid(raise_exception=True) # auto return 400
    interestSerializer.save()
    return Response(interestSerializer.data)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, id):
    instance = get_object_or_404(Interest, pk=id) #Application.objects.get(pk=id)
    Interest = request.data
    interestSerializer = InterestSerializer(instance, data=Interest)
    interestSerializer.is_valid(raise_exception=True)
    interestSerializer.save()
    return Response(InterestSerializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request):
    interest = Interest.objects.all()
    interestSerializer = InterestSerializer(interest, many=True) # many=True means 
    return JsonResponse(interestSerializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request, id):
    interest = get_object_or_404(Interest, pk=id)
    interestSerializer = InterestSerializer(interest) # many=True means 
    return JsonResponse(interestSerializer.data, safe=False)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    instance = get_object_or_404(Interest, pk=id)
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)