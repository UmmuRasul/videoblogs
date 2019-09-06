from django.urls import path
from .views import PostViewSet

app_name = "blogs"

urlpatterns = [
    
    path('post/', PostViewSet.as_view({'get': 'list'}), name='post'),
]