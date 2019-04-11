from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.core.files import File
from django.http import HttpResponse

from core.api.serializers import UserSerializer, GroupSerializer, ProfileSerializer
from easy_thumbnails.files import get_thumbnailer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from wsgiref.util import FileWrapper

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
        
        # check for valid input
        if profile_serializer.is_valid():
            file = profile_serializer.save()        

        content_type = request.FILES['photo'].content_type
        size = request.FILES['photo'].size
  
        # here we check for valid file type - jpg or png
        if content_type in ['image/png', 'image/jpg', 'image/jpeg']:
            
            # here we check for file size greater than 5 mb !
            if size > 5242880:
                return Response("Please upload file less than 5MB !")

            thumbnailer = get_thumbnailer(file.photo)
            large =  thumbnailer['large'] # 400 X 300
            # medium = thumbnailer['medium'] # 160 X 120
            # small = thumbnailer['small'] # 120 X 120
            filename = "thumbnail_" + request.FILES['photo'].name 
            response = HttpResponse(large, content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename={}'.format(filename)   

            return response            
        
        
        else:
            return Response("Please upload jpg or png files only.")
