from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.core.files import File
from django.http import HttpResponse

from core.api.serializers import UserSerializer, GroupSerializer, FileSerializer, ProfileSerializer
from easy_thumbnails.files import get_thumbnailer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .models import Profile

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows thumbnails to be generated.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def create(self, request, *args, **kwargs):
        profile_serializer = ProfileSerializer(data=request.data)
        if profile_serializer.is_valid():
            profile_serializer.save()        
        thumbnailer = get_thumbnailer(profile_serializer.data['photo'])
        large =  thumbnailer['large'] 
        # medium = thumbnailer['medium']
        # small = thumbnailer['small']
        return HttpResponse(large, content_type="image/png")
