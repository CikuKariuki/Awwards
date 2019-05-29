from rest_framework import serializers
from .models import Posts, Profile

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('images','caption','profile')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','email','profile','user','website','bio','phone')