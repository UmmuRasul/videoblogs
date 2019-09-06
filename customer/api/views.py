from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import NewSerializer, VideoSerializer
from customer.models import News, Video, ContactUs


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer