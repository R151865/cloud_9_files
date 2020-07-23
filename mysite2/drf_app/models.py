from datetime import datetime
from django.db import models
from rest_framework import serializers
# Create your models here.


class Comment(object):
    def __init__(self, content):
        self.content = content


"""
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance
"""

class EditItem(object):
    def __init__(self,name=None):
        self.name = name



class Profile(object):
    def __init__(self,name=None):
        self.name=name

class ProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length =100)


class User(object):
    def __init__(self, username):
        self.username =username

class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100)

class CommentSerializer(serializers.Serializer):
    
    content=serializers.CharField(max_length=100)
    user=UserSerializer()
    
    
    def create(self, validated_data):
        user_data=validated_data.pop('user')
        user=User(**user_data)
        comment=Comment(**validated_data)
        return comment
    



class BlogPost(object):
    def __init__(self, title=None, content=None):
        self.title=title
        self.content=content

class BlogPostSerializer(serializers.Serializer):
    title=serializers.CharField(max_length =100)
    content = serializers.CharField(max_length =100)

    def validate(self, data):
        if data['title'] < data['content']:
            raise serializers.ValidationError('Blog post is not about djanog')
        return data


class A(object):
    def __init__(self, score):
        self.score = score

def sulthan(value):
    if value % 2 != 0:
        raise serializers.ValidationError('sulthans error error')

def multiple_of_2(value):
    if value % 3 != 0:
        raise serializers.ValidationError('sulthans error error')

class ASerializer(serializers.Serializer):
    score =serializers.IntegerField(validators=[multiple_of_2,sulthan])