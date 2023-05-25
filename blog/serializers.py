from rest_framework import serializers
from .models import Blog
from topic1.serializers import TopicsSerializer

class BlogSerializer(serializers.ModelSerializer):
    topics = TopicsSerializer(read_only=True, many=True)
    class Meta:
        model = Blog
        fields = ('id','blogName', 'topics')