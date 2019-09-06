from rest_framework import serializers
from customer.models import News, Video

class NewSerializer(serializers.Serializer):
    class Meta:
        model = News
        fields = '__all__'

class VideoSerializer(serializers.Serializer):
    class Meta:
        model = Video
        fields = '__all__'