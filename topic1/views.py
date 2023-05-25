from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status

from .models import  Topics
from .serializers import TopicsSerializer



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    data = request.data # get data from resquest.
    topicSerializer = TopicsSerializer(data=data)
    topicSerializer.is_valid(raise_exception=True)
    topicSerializer.save()
    return Response(topicSerializer.data)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, id):
    topic = request.data
    instance = get_object_or_404(Topics, pk=id) #Application.objects.get(pk=id)
    topicSerializer = TopicsSerializer(instance, data=topic)
    topicSerializer.is_valid(raise_exception=True)
    topicSerializer.save()
    
    return Response(topicSerializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request):
    topics = Topics.objects.all()
    topicSerializer = TopicsSerializer(topics, many=True) # many=True means 
    return JsonResponse(topicSerializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request, id):
    topic = get_object_or_404(Topics, pk=id)
    personSerializer = TopicsSerializer(topic) # many=True means 
    return JsonResponse(personSerializer.data, safe=False)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    instance = get_object_or_404(Topics, pk=id)
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)