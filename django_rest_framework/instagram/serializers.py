from rest_framework.serializers import ModelSerializer 
from .models import Post
from rest_framework import serializers
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model() 
        fields = ['username','email']
class PostSerializer(ModelSerializer):
    # username = serializers.ReadOnlyField(source="author.username")
    author = AuthorSerializer()
    class Meta:
        model = Post
        fields =[

            'pk',
            'author',
            'message',
            'created_at',
            'updated_at',
        ]