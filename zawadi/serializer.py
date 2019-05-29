from rest_framework import serializers
from .models import Posts, Profile

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id','images','caption','profile')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','first_name','last_name','email','profile_picture','user','website','bio','phone')

