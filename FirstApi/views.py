from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from FirstApi.models import Post
from FirstApi.serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ItemSerializer