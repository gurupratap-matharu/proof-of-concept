from django.shortcuts import render
from django.contrib.auth.models import User, Group, Profile
from rest_framework import viewsets
from core.api.serializers import UserSerializer, GroupSerializer
from easy_thumbnails.files import get_thumbnailer


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
    thumbnailer = get_thumbnailer('animals/aardvark.jpg')
    thumbnail_options = {'crop': True}
    for size in (50, 100, 250):
        thumbnail_options.update({'size': (size, size)})
        thumbnailer.get_thumbnail(thumbnail_options)

    # or to get a thumbnail by alias
    thumbnailer['large']
    #Thumbnailer.generate_thumbnail()