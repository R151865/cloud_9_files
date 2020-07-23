from django.shortcuts import render

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CreateSnippetRequest:
    def __init__(self, code, title=''):
        self.code = code
        self.title = title

class CreateSnippetRequestSerializer(serializers.Serializer):
    code = serializers.CharField()
    title = serializers.CharField(
        allow_null=True, required=False, allow_blank=True
    )
    
    def create(self, validated_data):
        return CreateSnippetRequest(**validated_data)

class CreateSnippetResponse:
    def __init__(self, id, code, title=''):
        self.code = code
        self.title = title
        self.id = id

def create_snippet_in_db(title, code):
    from snippets.models import Snippet
    return Snippet.objects.create(title=title, code=code)


class CreateSnippetResponseSerializer(serializers.Serializer):
    code = serializers.CharField()
    title = serializers.CharField(
        allow_null=True, required=False, allow_blank=True
    )
    id = serializers.IntegerField()
    def create(self, validated_data):
        return CreateSnippetRequest(**validated_data)
def get_all():
    from snippets.models import Snippet
    return Snippet.objects.all()


@api_view(['POST','GET'])
def dummy_view(request):
    if request.method=='GET':
        serializer = CreateSnippetResponseSerializer(get_all(), many=True)
        return Response(serializer.data)
    print('************************   sulthan   *******************************')
    print('Hellow World!')
    serializer = CreateSnippetRequestSerializer(data=request.data)
    is_invalid_data = not serializer.is_valid()
    if is_invalid_data:
        return Response(serializer.errors, status=400)
        
    request_obj = serializer.save()
        
    new_snippet_obj =  create_snippet_in_db(request_obj.title, request_obj.code)
    serializer = CreateSnippetResponseSerializer(new_snippet_obj)
        
    return Response(serializer.data,status=200)
