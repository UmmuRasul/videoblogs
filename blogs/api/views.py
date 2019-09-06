from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer
from blogs.models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
