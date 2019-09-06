from django.urls import path
from .views import VideoViewSet, NewsViewSet

app_name = "customer"

urlpatterns = [
    
    path('video/', VideoViewSet.as_view({'get': 'list'}), name='video'),
    path('news/', NewsViewSet.as_view({'get': 'list'}), name='news'),
    

]