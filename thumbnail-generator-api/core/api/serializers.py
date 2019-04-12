from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Our User serializer class that generates user serializer based on
    user models in the database.
    """
    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Generates a group serializer from the groups in which users are defined into.
    """
    class Meta:
        model = Group
        fields = '__all__'
    
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """
    Generates profile serializers for our thumbnails.
    """
    class Meta():
        model = Profile
        fields = '__all__'
