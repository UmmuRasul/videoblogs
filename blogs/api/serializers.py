from rest_framework import serializers
from blogs.models import Post

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = '__all__'