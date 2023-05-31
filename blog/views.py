from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status

from .models import  Blog
from .serializers import BlogSerializer
from topic1.models import Topics

import logging

logger = logging.getLogger('django')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def blogCreate(request):
    blog = request.data # get data from resquest.
    print(blog["topics"])
    newBlog = Blog.objects.create(
        blogName=blog["blogName"])
    newBlog.save()

    for topic in blog["topics"]:
        topicObject = get_object_or_404(Topics, pk=topic)
        newBlog.topics.add(topicObject)
    
    
    blogSerializer = BlogSerializer(newBlog)

    return Response(blogSerializer.data)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def blogUpdate(request, id):
    blog = request.data
    instance = get_object_or_404(Blog, pk=id) #Application.objects.get(pk=id)
    blogSerializer = BlogSerializer(instance, data=blog)
    blogSerializer.is_valid(raise_exception=True)
    blogSerializer.save()
    
    updateTopics = []
    for topicId in blog["topics"]:
        print(topicId)
        topic_obj = get_object_or_404(Topics, pk=topicId) 
        updateTopics.append(topic_obj)
    instance.topics.set(updateTopics)
    return Response(blogSerializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request):
    """
    List all topics
    """
    logger.info("Platform is running FINE")
    logger.warning("Platform is running at risk")
    logger.debug("Platform is running at risk")
    logger.error("Error Platform is running at risk")
    blogs = Blog.objects.all()
    blogSerializer = BlogSerializer(blogs, many=True) # many=True means 
    return JsonResponse(blogSerializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blogSerializer = BlogSerializer(blog) # many=True means 
    return JsonResponse(blogSerializer.data, safe=False)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    instance = get_object_or_404(Blog, pk=id)
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)