from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import File, Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model = Profile
        fields = '__all__'
