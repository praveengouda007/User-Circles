from rest_framework.serializers import ModelSerializer
from .models import Circle, CircleUser
from django.contrib.auth.models import User
from rest_framework import serializers

class CircleUserSerializer(ModelSerializer):
    class Meta:
        model = CircleUser
        fields = ['circle','name','role', 'users']

class CircleSerializer(ModelSerializer):
    class Meta:
        model = Circle
        fields = ['name', 'description', 'image', 'created_by']
