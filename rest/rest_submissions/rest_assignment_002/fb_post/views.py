from django.shortcuts import render


from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.decorators import protected_resource

from rest_framework.decorators import api_view, authentication_classes

from rest_framework import serializers
from rest_framework.response import Response

from .exceptions import *

from fb_post.constants import ReactionChoices
from fb_post.utils.create_post import create_post as get_create_post
from fb_post.utils.get_post import get_post as function_to_get_post
from fb_post.utils.reply_to_comment import reply_to_comment as function_to_reply_to_comment
from fb_post.utils.react_to_post import react_to_post as function_to_react_to_post
from fb_post.utils.react_to_comment import react_to_comment as function_to_react_to_comment
from fb_post.utils.delete_post import delete_post as function_to_delete_post
from fb_post.utils.create_comment import create_comment as function_to_create_comment



LIST_OF_REACTION_TYPE_CHOICES = [
    reaction_choice.value for reaction_choice in ReactionChoices
    ]


# Task - 1
class CreatePostRequest:
    def __init__(self, user_id, content=''):
        self.user_id = user_id
        self.content = content


class CreatePostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content =  serializers.CharField(
        required=False, allow_blank=True
    )

    def create(self, validated_data):
        return CreatePostRequest(**validated_data)


class CreatePostIdResponse:
    def __init__(self, post_id):
        self.post_id = post_id


class CreatePostIdResponseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return CreatePostIdResponse(**validated_data)


@api_view(['POST'])
def create_post(request):

    post_serializer = CreatePostRequestSerializer(data=request.data)
    is_invalid_data = not post_serializer.is_valid()

    if is_invalid_data:
        return Response(post_serializer.errors,status=400)
    post_serializer_obj = post_serializer.save()
        
    try:
        post_id = get_create_post(
            post_serializer_obj.user_id,
            post_serializer_obj.content
        )
    except InvalidUserException:
        return Response(status=404)
    except InvalidPostContent:
        return Response(status=400)

    create_post_id_obj = CreatePostIdResponse(post_id)
    post_id_obj_dict = CreatePostIdResponseSerializer(create_post_id_obj)
    return Response(post_id_obj_dict.data,status=201)



# Task - 2
@api_view(['GET'])
@authentication_classes([OAuth2Authentication])
#@protected_resource(['superuser'])
def get_post(request,post_id):
    print(post_id)
    try:
        post_dict = function_to_get_post(post_id)
    except InvalidPostException:
        return Response(status=404)
    serializer = CheckPostDetailsSerializer(data=post_dict)
    is_invalid_data = not serializer.is_valid()
    if is_invalid_data:
        return Response(serializer.errors,status=400)
    
    return Response(post_dict, status=200)
    


class UserClassSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    name =  serializers.CharField(max_length=100)
    profile_pic = serializers.CharField(
        allow_blank=True
        )

class ReactionsSerializer(serializers.Serializer):

    count = serializers.IntegerField()
    type = serializers.ListField(
        child=serializers.ChoiceField(
            choices=LIST_OF_REACTION_TYPE_CHOICES
        ), max_length=100
    )

class ReplyClassSerializer(serializers.Serializer):

    comment_id =  serializers.IntegerField()
    commenter= UserClassSerializer()
    commented_at = serializers.DateTimeField()
    comment_content = serializers.CharField(max_length=1000)
    reactions = ReactionsSerializer()


class CommentClassSerializer(serializers.Serializer):
    
    comment_id =  serializers.IntegerField()
    commenter= UserClassSerializer()
    commented_at = serializers.DateTimeField()
    comment_content = serializers.CharField(max_length=1000,)
    reactions = ReactionsSerializer()
    replies_count = serializers.IntegerField()
    replies = ReplyClassSerializer(many=True)


class CheckPostDetailsSerializer(serializers.Serializer):

    post_id = serializers.IntegerField()
    posted_by = UserClassSerializer()
    posted_at = serializers.DateTimeField()
    comments = serializers.ListField(
        child=CommentClassSerializer()
        )
    #comments = CommentClassSerializer(many=True)
    reactions = ReactionsSerializer()
    comments_count = serializers.IntegerField()
    


# Task 3
@api_view(['POST'])
def reply_to_comment(request, comment_id):
    reply_serializer = ReplyToCommentRequestSerializer(data=request.data)
    
    is_invalid_data = not reply_serializer.is_valid()
    
    if is_invalid_data:
        return Response(reply_serializer.errors,status=400)
    reply_serializer_obj = reply_serializer.save()
    try:
        reply_id = function_to_reply_to_comment(
            reply_serializer_obj.user_id,
            comment_id,
            reply_serializer_obj.content,
            )
    except InvalidUserException:
        return Response(status=404)
    except InvalidCommentException:
        return Response(status=404)
    except InvalidReplyContent:
        return Response(status=400)

    reply_obj = ReplyToCommentResponse(reply_id)    
    reply_obj_serializer = ReplyToCommentResponseSerializer(reply_obj)

    return Response(reply_obj_serializer.data,status=201)



class ReplyToCommentRequest:
    def __init__(self, user_id, content=''):
        self.user_id = user_id
        self.content = content


class ReplyToCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField(
        required=False, allow_blank=True, max_length=1000
    )
    
    def create(self, validated_data):
        return ReplyToCommentRequest(**validated_data)

class ReplyToCommentResponse:
    def __init__(self, reply_id):
        self.reply_id = reply_id

class ReplyToCommentResponseSerializer(serializers.Serializer):
    reply_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return ReplyToCommentResponse(**validated_data)



# Task 4
@api_view(['POST'])
def react_to_post(request,post_id):

    react_to_post_serializer = ReactToPostRequestSerializer(
        data = request.data
        )
    is_invalid_data = not react_to_post_serializer.is_valid()
    
    if is_invalid_data:
        return Response(react_to_post_serializer.errors)
    
    react_to_post_obj = react_to_post_serializer.save()
    try:
        function_to_react_to_post(
            react_to_post_obj.user_id,
            post_id,
            react_to_post_obj.reaction_type
        )
    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)
    except InvalidReactionTypeException:
        return Response(status=400)

    return Response(status=200)


class ReactToPostRequest:
    
    def __init__(self, user_id, reaction_type):
        self.user_id = user_id
        self.reaction_type = reaction_type

class ReactToPostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    reaction_type = serializers.ChoiceField(
        choices = LIST_OF_REACTION_TYPE_CHOICES
    )
    
    def create(self, validated_data):
        return ReactToPostRequest(**validated_data)



# Task 5
@api_view(['POST'])
def react_to_comment(request,comment_id):

    react_to_comment_serializer = ReactToCommentRequestSerializer(
        data = request.data
    )
    is_invalid_data = not react_to_comment_serializer.is_valid()

    if is_invalid_data:
        return Response(react_to_comment_serializer.errors)
    react_to_comment_obj = react_to_comment_serializer.save()
    try:
        function_to_react_to_comment(
            react_to_comment_obj.user_id,
            comment_id,
            react_to_comment_obj.reaction_type
        )
    except InvalidUserException:
        return Response(status=404)
    except InvalidCommentException:
        return Response(status=404)
    except InvalidReactionTypeException:
        return Response(status=400)

    return Response(status=200)

class ReactToCommentRequest:
    
    def __init__(self, user_id, reaction_type):
        self.user_id = user_id
        self.reaction_type = reaction_type

class ReactToCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    reaction_type = serializers.ChoiceField(
        choices = LIST_OF_REACTION_TYPE_CHOICES
    )
    
    def create(self, validated_data):
        return ReactToCommentRequest(**validated_data)


# Task 6
@api_view(['POST'])
def delete_post(request, post_id):
    delete_post_serializer = DeletePostRequestSerializer(
        data = request.data
    )
    
    is_invalid_data = not delete_post_serializer.is_valid()
    if is_invalid_data:
        return Response(delete_post_serializer.errors,status=400)
    delete_post_obj = delete_post_serializer.save()
    try:
        function_to_delete_post(
            delete_post_obj.user_id,
            post_id
        )
    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)
    except UserCannotDeletePostException:
        return Response(status=403)

    return Response(status=200)

class DeletPostRequest:
    def __init__(self, user_id):
        self.user_id = user_id

class DeletePostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return DeletPostRequest(**validated_data)

# Task 7

class CreateCommentRequest:
    def __init__(self, user_id, content=''):
        self.user_id = user_id
        self.content = content

class CreateCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content =  serializers.CharField(
        required=False, allow_blank=True
        )
    def create(self, validated_data):
        return CreateCommentRequest(**validated_data)
    
class CreateCommentIdResponse:
    def __init__(self, comment_id):
        self.comment_id = comment_id


class CreateCommentIdResponseSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return CreateCommentIdResponse(**validated_data)




@api_view(['POST'])
def create_comment(request, post_id):

    create_comment_serializer = CreateCommentRequestSerializer(data=request.data)
    is_invalid_data = not create_comment_serializer.is_valid()

    if is_invalid_data:
        return Response(create_comment_serializer.errors)
        
    create_comment_obj = create_comment_serializer.save()
    try:
        comment_id = function_to_create_comment(
            create_comment_obj.user_id,
            post_id,
            create_comment_obj.content
        )
    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)
    except InvalidCommentContent:
        return Response(status=400)

    create_comment_id_obj = CreateCommentIdResponse(comment_id)
    comment_id_obj_dict = CreateCommentIdResponseSerializer(create_comment_id_obj)
    return Response(comment_id_obj_dict.data,status=201)
