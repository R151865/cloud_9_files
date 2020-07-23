from django.shortcuts import render

from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response

from fb_post.utils.create_post import create_post as get_create_post
# Create your views here.

class CreateUser:
    def __init__(self, name, profile_pic=''):
        self.name = name
        self.profile_pic = profile_pic

class CreateUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    profile_pic = serializers.CharField(
        required=False, allow_blank=True
    )
    
    def create(self, **validated_data):
        return CreateUser(**validated_data)


# Task - 1

class CreatePostRequest:
    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content


class CreatePostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content =  serializers.CharField()


    def create(self, validated_data):
        return CreatePostRequest(**validated_data)
class CreatePostIdResponse:
    def __init__(self, post_id):
        self.post_id = post_id


class CreatePostIdResponseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return CreatePostId(**validated_data)




@api_view(['POST'])
def create_post(request):
    post_serializer = CreatePostRequestSerializer(data=request.data)
    if post_serializer.is_valid():
        post_serializer_obj = post_serializer.save()
        
        post_id=get_create_post(
            user_id=post_serializer_obj.user_id,
            post_content=post_serializer_obj.content
        )
        create_post_id_obj = CreatePostIdResponse(post_id)
        serializer = CreatePostIdResponseSerializer(create_post_id_obj)
        return Response(serializer.data)
        
