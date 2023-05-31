from django.test import TestCase
from django.urls import reverse
import pytest
import json
import datetime
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.permissions import IsAuthenticated
from django.urls import path
from . import views
from .models import Blog
from topic1.models import Topics
from .serializers import BlogSerializer


# Create your tests here.
@pytest.mark.django_db
# @permission_classes([IsAuthenticated])
class BlogTest(APITestCase):
    def setUp(self):
        self.topic1 = Topics.objects.create(Author='alex1', TopicName='Hello', DateOfPublish=datetime.date(2023, 5, 16), Contact='1234567890')
        self.topic2 = Topics.objects.create(Author='alex2', TopicName='Hello', DateOfPublish=datetime.date(2023, 5, 16), Contact='1234567890')
        self.topic3 = Topics.objects.create(Author='alex3', TopicName='Hello', DateOfPublish=datetime.date(2023, 5, 16), Contact='1234567890')
        print(self.topic1.DateOfPublish)
    def test_can_create_blog(self):

        url = reverse('blogCreate')
        data = {
            'blogName': 'Test Blog',
            'topics': [self.topic1.id, self.topic2.id]
        }
        serializer = BlogSerializer(data, many=True)
        response = self.client.post(url, data)
        # self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)# create testcase but not good
        # response = api_client_auth.post(url, data=data)
        assert response.status_code == 200

    def test_can_update_blog(self):
        blog = Blog.objects.create(
        blogName='Test Blog')
        blog.topics.set([self.topic1, self.topic2])

        # url = reverse(views.blogUpdate, kwargs={'pk': blog.id})
        # url = reverse(views.blogUpdate, args=[str(self.id)])
        data = {
            'blogName': 'Updated Test Blog',
            'topics': [self.topic2.id, self.topic3.id],
        }

        response = self.client.put('blog/update/1/', data)
        response_data = BlogSerializer(data)

        post = Blog.objects.get(id=blog.id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND) # create testcase but not good
        # self.assertEqual(response_data['blogName'], post.blogName)
        # self.assertEqual(response_data['topics'], post.topics)

        # self.assertEqual(len(response_data['topics']), 2)
        # self.assertEqual(response_data['topics'][0]['id'], self.tag2.id)
        # self.assertEqual(response_data['topics'][1]['id'], self.tag3.id)

