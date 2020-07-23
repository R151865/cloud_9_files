
# Create your tests here.

# create user post
# 1.test_create_post_with_valid_details
# 2.test_create_post_with_invalid_details may be datatypes
# 3.test_create_post__raise error when user_id_does_not_exit
# 4. test_create_post raise error when
# 5. test_create_post when raise error when post_content_exactly empty

# create comment

#1.test create comment with valid details
# 2. test create comment in valid user id raise error
# 3 .test create comment  in valid post id raise error 
# 4 .test create comment  in comment content empty == ""d raise error 

# reply_to_comment
    
#1.test reply to comment with valid data
# 2. test reply to comment in valid data raise error()
#3 .test reply to comment reply comment is == empty only
# test reply to comment when comment has parent comment id
# test reply to comment when when parent has no comment id

#react to post

#1. test react to post raise error when  user id ,post id , reaction type are in valid
#2.test react  to post    with valid details 
#3.test react  to post  if user reacting at first time
#4.test react to post update react when user react with different react type
#5.test react to post  deleting the react when user reacting same react type

#react to comment

#1. test react to comment raise error when  user id ,post id , reaction type are in valid
#2.test react  to comment     with valid details 
#3.test react  to comment   if user reacting at first time
#4.test react to comment  update react when user react with different react type
#5.test react to comment   deleting the react when user reacting same react type


# total reaction_count
# test total reaction count whether is it giving integer 
# test total reaction count  whether are we getting count from reaction model or not
 
# get reaction metrics

# test get reaction metrics raise error when post id not valid
# test get reaction metrics for valid details
# test get reaction metrics whether am i getting  it from reaction models or not 
# test get reaction metrics whether am i getting correct out put

# delete post

#1.test delete post  with valid details
# 2. test delete post with in valid details raise error

# get post with more positive reactions
#1. test get post with more positive reactions with valid details(use parametrize)

# get reaction to post

#1.get reaction to post  with valid details  and checking the dict format 
#2. get reaction to post with invalid details 


# get post
#1. get post with valid details
# 2. get post with in valid details raise error

# get user posts
#1. get user posts with valid details
# 2. get user posts with in valid details raise error


# get replies for comment
#1. get replies for comment with valid details
# 2. get replies for comment with in valid details raise error





from django.test import TestCase
from freezegun import freeze_time
import datetime
import pytest
from .models import *
from  .utils import *
from django.utils import timezone
from .constants import *

pytestmark=pytest.mark.django_db



users_list=[
        {'name':'sulthan',      'profile_pic':'sulthan_babu/profile_pic'},
        {'name':'randy orton',  'profile_pic':'randyorton/profile_pic'},
        {'name':'elon musk',     'profile_pic':'elonmusk/profile_pic'},
        {'name':'sravani',      'profile_pic':'sravani/profile_pic'},
        {'name':'che quevara',  'profile_pic':'chequeara/profile_pic'},
        {'name':'shajahan',     'profile_pic':'shajahan/profile_pic'}
    ]

posts_list=[
        {'posted_by_id':1, 'content':'empty'},
        {'posted_by_id':1, 'content':'empty'},
        {'posted_by_id':2, 'content':'empty3'},
        {'posted_by_id':2, 'content':'empty4'},
        {'posted_by_id':3, 'content':'empty5'},
        {'posted_by_id':3, 'content':'empty6'},
        {'posted_by_id':4, 'content':'empty7'},
        {'posted_by_id':4, 'content':'empty8'},
        {'posted_by_id':5, 'content':'empty9'},
        {'posted_by_id':1, 'content':'empty'}
    
    ]

comments_list=[
        {'commented_by_id':3,'post_id':1,'content':'this is comment','parent_comment_id':None},
        {'commented_by_id':1,'post_id':1,'content':'this is comment','parent_comment_id':None},
        {'commented_by_id':3,'post_id':1,'content':'this is comment','parent_comment_id':2},
        {'commented_by_id':4,'post_id':1,'content':'this is comment','parent_comment_id':1},
        {'commented_by_id':5,'post_id':3,'content':'this is comment','parent_comment_id':1},
        {'commented_by_id':2,'post_id':3,'content':'this is comment','parent_comment_id':None},
        {'commented_by_id':3,'post_id':4,'content':'this is comment','parent_comment_id':5},
        {'commented_by_id':5,'post_id':2,'content':'this is comment','parent_comment_id':None},
        {'commented_by_id':5,'post_id':2,'content':'this is comment','parent_comment_id':8}
    ]
    
reactions_list=[
    {'reacted_by_id':1,'post_id':1,'comment_id':None,'reaction':ReactionChoices.WOW.value},
    {'reacted_by_id':5,'post_id':1,'comment_id':None,'reaction':ReactionChoices.WOW.value},
    {'reacted_by_id':3,'post_id':1,'comment_id':None,'reaction':ReactionChoices.LOVE.value},
    {'reacted_by_id':4,'post_id':1,'comment_id':None,'reaction':ReactionChoices.SAD.value},
    
    {'reacted_by_id':3,'post_id':2,'comment_id':None,'reaction':ReactionChoices.ANGRY.value},
    {'reacted_by_id':4,'post_id':3,'comment_id':None,'reaction':ReactionChoices.SAD.value},
    
    {'reacted_by_id':5,'post_id':4,'comment_id':None,'reaction':ReactionChoices.WOW.value},
    {'reacted_by_id':5,'post_id':4,'comment_id':None,'reaction':ReactionChoices.WOW.value},
    
    {'reacted_by_id':3,'post_id':7,'comment_id':None,'reaction':ReactionChoices.THUMBS_UP.value},
    
    {'reacted_by_id':6,'post_id':9,'comment_id':None,'reaction':ReactionChoices.HAHA.value},
    {'reacted_by_id':4,'post_id':9,'comment_id':None,'reaction':ReactionChoices.THUMBS_DOWN.value},
    
    
    
    {'reacted_by_id':1,'post_id':None,'comment_id':1,'reaction':ReactionChoices.WOW.value},
    {'reacted_by_id':5,'post_id':None,'comment_id':1,'reaction':ReactionChoices.LOVE.value},
    {'reacted_by_id':3,'post_id':None,'comment_id':1,'reaction':ReactionChoices.LOVE.value},
    {'reacted_by_id':4,'post_id':None,'comment_id':1,'reaction':ReactionChoices.SAD.value},
    
    {'reacted_by_id':3,'post_id':None,'comment_id':2,'reaction':ReactionChoices.WOW.value},
    {'reacted_by_id':4,'post_id':None,'comment_id':3,'reaction':ReactionChoices.ANGRY.value},
    {'reacted_by_id':5,'post_id':None,'comment_id':4,'reaction':ReactionChoices.LIT.value},
]


@pytest.fixture
@freeze_time("2012-01-14")
def data_pop():
    
    user_objs=User.objects.bulk_create(
        [User(name=user['name'],profile_pic=user['profile_pic']) for user in users_list ]
        )
    
    post_objs=Post.objects.bulk_create(
        [Post(posted_by_id=post['posted_by_id'],content=post['content']) for post in posts_list]
        )
    
    comment_objs=Comment.objects.bulk_create(
        [Comment(
            commented_by_id=comment['commented_by_id'],
            content=comment['content'] ,
            post_id=comment['post_id'],
            parent_comment_id =comment['parent_comment_id']
        )
        for comment in comments_list
        ]
    )
    
    reaction_objs=Reaction.objects.bulk_create(
        [Reaction(
                reacted_by_id=reaction['reacted_by_id'],
                post_id=reaction['post_id'],
                comment_id=reaction['comment_id'],
                reaction=reaction['reaction']
        )
        for reaction in   reactions_list 
        ]
    )
    
    dict_data={
        'user_objs':user_objs,
        'post_objs':post_objs,
        'comment_objs':comment_objs,
        'reaction_objs':reaction_objs
    }
    
    return dict_data
    


# Task - 2
@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_create_post_with_valid_details_return_post_id(data_pop):
    
    # Arrange
    user_id=1
    post_content= 'This is john cena content'    
    
    # Act
    post_id = create_post(user_id, post_content)
    
    # Assert
    post=Post.objects.get(pk=post_id)
    
    assert post.id == post_id
    assert post.posted_by_id == user_id
    assert post.content == post_content
    assert post.posted_at == timezone.now()


def test_create_post_when_invalid_user_id_raise_invalid_user_exception(data_pop):
    
    # Arrange
    user_id=0
    post_content ='this is post_content'
    
    # Act
    
    # Assert
    with pytest.raises(InvalidUserException):
        assert create_post(user_id, post_content)
    
   
def test_create_post_when_invalid_post_content_raise_invalid_post_content(data_pop):
    
    # Arrange
    user_id=1
    post_content =''
    
    # Act
    
    # Assert
    with pytest.raises(InvalidPostContent):
        assert create_post(user_id, post_content)
    


# Task - 3
@pytest.mark.django_db
@freeze_time("2012-01-14")
class TestCreateComment:
    
    def test_create_comment_with_valid_details_return_comment_id(self,data_pop):
        
        # Arrange
        post_id=1
        user_id=2
        comment_content='this is comment content'
        
        # Act
        comment_id=create_comment(user_id, post_id, comment_content)
        
        # Assert
        comment = Comment.objects.get(pk = comment_id)
       
        assert comment.id == comment_id
        assert comment.content ==  comment_content
        assert comment.post_id ==  post_id
        assert comment.commented_by_id ==  user_id
        assert comment.commented_at ==  timezone.now()
        
    def test_create_comment_when_invalid_user_id_raise_invalid_user_exception(self,data_pop):
        
        # Arrange
        user_id =0
        post_id=1
        comment_content='this is comment content'
        
        # Act
        
        # Assert
        with pytest.raises(InvalidUserException):
            assert create_comment(user_id, post_id, comment_content)
    
    def test_create_comment_when_invalid_post_id_raise_invalid_post_exception(self,data_pop):
        
        # Arrange
        user_id =1
        post_id=0
        comment_content='this is comment content'
        
        # Act
        
        # Assert
        with pytest.raises(InvalidPostException):
            assert create_comment(user_id, post_id, comment_content)
    
    def test_create_comment_when_invalid_comment_content_raise_invalid_comment_content(self,data_pop):
        
        # Arrange
        user_id = 1
        post_id=2
        comment_content=''
        
        # Act
        
        # Assert
        with pytest.raises(InvalidCommentContent):
            assert create_comment(user_id, post_id, comment_content)
    
        

# Task - 4
# reply_to_comment

@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_reply_to_comment_when_comment_with_valid_details_create_reply_to_comment_and_return_reply_id(data_pop):
    
     # Arrange
     comment_id=8
     user_id=1
     reply_content='this is reply content'
     comment=Comment.objects.get(pk=comment_id)
     
     # Act
     reply_id=reply_to_comment(user_id, comment_id, reply_content)
     
     # Assert
     reply=Comment.objects.get(pk=reply_id)
     
     assert reply.id ==  reply_id
     assert reply.commented_by_id == user_id
     assert reply.content == reply_content
     assert reply.commented_at == timezone.now()
     assert reply.parent_comment_id == comment_id
     assert comment.parent_comment_id == None
     
     
@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_reply_to_comment_for_reply_with_valid_details_return_new_reply_id(data_pop):
     
     # Arrange
     parent_id=1
     comment_id=4
     user_id=3
     reply_content='this is reply'
    
     parent_comment=Comment.objects.get(pk= parent_id)
     comment=Comment.objects.get(pk= comment_id )
    
     # Act
     reply_id=reply_to_comment(user_id, comment_id, reply_content)
     
     # Assert
     reply=Comment.objects.get(pk=reply_id)
     
     assert reply.id ==  reply_id
     assert reply.commented_by_id == user_id
     assert reply.content == reply_content
     assert reply.commented_at == timezone.now()
     assert reply.parent_comment_id == parent_comment.id
     assert comment.parent_comment_id == parent_comment.id
     assert parent_comment.parent_comment_id is  None 
     
@pytest.mark.django_db
def test_reply_to_comment_when_invalid_user_id_raise_invalid_user_exception(data_pop):
    
    # Arrage
    user_id = 0
    comment_id=1
    reply_content ='reply content'
    
    # Act
     
    # Assert
    with pytest.raises(InvalidUserException):
        assert reply_to_comment(user_id, comment_id, reply_content)
    
@pytest.mark.django_db
def test_reply_to_comment_when_invalid_comment_id_raise_invalid_comment_exception(data_pop):
    
    # Arrage
    user_id = 1
    comment_id=0
    reply_content ='reply content'
        
    # Act
     
    # Assert
    with pytest.raises(InvalidCommentException):
        assert reply_to_comment(user_id, comment_id, reply_content)
    
@pytest.mark.django_db
def test_reply_to_comment_when_invalid_reply_content_raise_invalid_reply_content(data_pop):
    
    # Arrage
    user_id = 1
    comment_id=2
    reply_content =""
        
    # Act
     
    # Assert
    with pytest.raises(InvalidReplyContent):
        assert reply_to_comment(user_id, comment_id, reply_content)
    


# Task - 5
#react to post

@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_react_to_post_with_valild_details_react_to_post(data_pop):
    
    # Arrange
    post_id=9
    user_id=1
    reaction_type=ReactionChoices.WOW.value
    
    # Act
    react_to_post(user_id, post_id, reaction_type)
    
    # Assert
    reaction=Reaction.objects.all().last()
    
    assert reaction.reaction == reaction_type
    assert reaction.post_id == post_id
    assert reaction.reacted_by_id  == user_id
    assert reaction.reacted_at == timezone.now()


@pytest.mark.django_db
@freeze_time("2012-01-14")
@pytest.mark.parametrize('reaction_type,updated_reaction_type',[
    (ReactionChoices.LIT.value,ReactionChoices.THUMBS_DOWN.value),
    (ReactionChoices.THUMBS_DOWN.value,ReactionChoices.LIT.value),
    (ReactionChoices.ANGRY.value,ReactionChoices.SAD.value)
    ])
def test_react_to_post_when_different_reaction_type_given_by_same_user_update_reaction(data_pop,updated_reaction_type,reaction_type):
   
    # Arrange
    post_id=10
    user_id=6
    reaction_type=reaction_type
    updated_reaction_type =updated_reaction_type
    react_to_post(user_id, post_id, reaction_type)
    
    # Act
    react_to_post(user_id, post_id, updated_reaction_type)
    
    # Assert
    reaction=Reaction.objects.all().last()
    
    assert reaction.reaction == updated_reaction_type
    assert reaction.post_id == post_id
    assert reaction.reacted_by_id  == user_id
    assert reaction.reacted_at == timezone.now()
    

@pytest.mark.django_db
def test_react_to_post_when_same_reactions_given_by_same_user_delete_reaction(data_pop):
   
    # Arrange
    post_id=10
    user_id=6
    reaction_type=ReactionChoices.LOVE.value
    same_reaction_type=ReactionChoices.LOVE.value
    react_to_post(user_id, post_id, reaction_type)
    
    # Act
    react_to_post(user_id, post_id, same_reaction_type)
    
    # Assert
    deleted_reaction_return_false=Reaction.objects.filter(
        reacted_by_id=user_id,
        post_id=post_id,
        reaction= reaction_type
    ).exists()
    
    assert deleted_reaction_return_false is  False
    
@pytest.mark.django_db
def test_react_to_post_when_invalid_user_id_raise_invalid_user_exception(data_pop):
    
    # Arrange
    post_id=2
    user_id=0
    reaction_type=ReactionChoices.LOVE.value
    
    # Act
    
    # Assert
    with pytest.raises(InvalidUserException):
        assert react_to_post(user_id, post_id, reaction_type)
    

@pytest.mark.django_db
def test_react_to_post_when_invalid_post_id_raise_invalid_post_exception(data_pop):
   
    # Arrange
    post_id=0
    user_id=2
    reaction_type=ReactionChoices.LOVE.value
    
    # Act
    
    # Assert
    with pytest.raises(InvalidPostException):
        assert react_to_post(user_id, post_id, reaction_type)
    

@pytest.mark.django_db
def test_react_to_post_when_invalid_reaction_type_raise_invalid_reaction_type(data_pop):
    
    # Arrange
    post_id=1
    user_id=2
    reaction_type='NAMASTE reaction'
    
    # Act
    
    # Assert
    with pytest.raises(InvalidReactionTypeException):
        assert react_to_post(user_id, post_id, reaction_type)
    

# Task - 6
#react to comment

@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_react_to_comment_with_valild_details_react_to_comment(data_pop):
    
    # Arrange
    comment_id=1
    user_id=2
    reaction_type=ReactionChoices.LIT.value
    
    # Act
    react_to_comment(user_id, comment_id, reaction_type)
    
    # Assert
    reaction=Reaction.objects.all().last()
    
    assert reaction.reaction == reaction_type
    assert reaction.comment_id == comment_id 
    assert reaction.reacted_by_id  == user_id
    assert reaction.reacted_at == timezone.now()


@pytest.mark.django_db
@freeze_time("2012-01-14")
@pytest.mark.parametrize('reaction_type,updated_reaction_type',[
    (ReactionChoices.LIT.value,ReactionChoices.THUMBS_DOWN.value),
    (ReactionChoices.THUMBS_DOWN.value,ReactionChoices.LIT.value),
    (ReactionChoices.ANGRY.value,ReactionChoices.SAD.value)
     ])
def test_react_to_comment_when_diffent_reactions_given_by_same_user_update_reaction(data_pop,updated_reaction_type,reaction_type):
    
    # Arrange
    comment_id=1
    user_id=6
    reaction_type=reaction_type
    updated_reaction_type =updated_reaction_type
    react_to_comment(user_id, comment_id, reaction_type)
    
    # Act
    react_to_comment(user_id, comment_id, updated_reaction_type)
    
    # Assert
    reaction=Reaction.objects.all().last()
    
    assert reaction.reaction == updated_reaction_type
    assert reaction.comment_id == comment_id
    assert reaction.reacted_by_id  == user_id
    assert reaction.reacted_at == timezone.now()
    


@pytest.mark.django_db
def test_react_to_comment_delete_reaction_type_when_same_reaction_type_given_by_same_user(data_pop):
    
    # Arrange
    comment_id=1
    user_id=6
    reaction_type=ReactionChoices.LOVE.value
    same_reaction_type=ReactionChoices.LOVE.value
    react_to_comment(user_id, comment_id, reaction_type)
    
    # Act
    react_to_comment(user_id, comment_id, same_reaction_type)
        
    # Assert
    deleted_reaction_return_false=Reaction.objects.filter(
        reacted_by_id=user_id,
        comment_id=comment_id,
        reaction= reaction_type
    ).exists()
    
    assert deleted_reaction_return_false is  False

@pytest.mark.django_db
def test_react_to_comment_when_invalid_user_id_raise_invalid_user_exception(data_pop):
    
    # Arrange
    comment_id=1
    user_id=0
    reaction_type=ReactionChoices.LOVE.value
    
    # Act
    
    # Assert
    with pytest.raises(InvalidUserException):
        assert react_to_comment(user_id, comment_id, reaction_type)
    

@pytest.mark.django_db
def test_react_to_comment_when_invalid_post_id_raise_invalid_user_exception(data_pop):
    
    # Arrange
    comment_id=0
    user_id=1
    reaction_type=ReactionChoices.LOVE.value
    
    # Act
    
    # Assert
    with pytest.raises(InvalidCommentException):
        assert react_to_comment(user_id, comment_id, reaction_type)
    

@pytest.mark.django_db
def test_react_to_comment_when_invalid_reaction_type_raise_invalid_reaction_type(data_pop):
    
    # Arrange
    comment_id=1
    user_id=3
    reaction_type='NAMASTE reaction'
    
    # Act
    
    # Assert
    with pytest.raises(InvalidReactionTypeException):
        assert react_to_comment(user_id, comment_id, reaction_type)
    
# Task - 7
# total reaction_count

@pytest.mark.django_db
def test_total_reaction_count_with_valid_details_return_count(data_pop):
   
    # Arrage
    expected_dict={'count':18}
    
    # Act
    actual_dict=get_total_reaction_count()
   
    # Assert
    assert actual_dict == expected_dict
    
@pytest.mark.django_db
def test_total_reaction_count_when_no_reactions_in_database_return_count_zero():
    
    # Arrage
    expected_dict={'count':0}
    
    # Act
    actual_dict=get_total_reaction_count()
    
    # Assert
    assert actual_dict == actual_dict
    
# Task - 8   
# get reaction metrics

@pytest.mark.django_db
def test_get_reaction_metrics_with_valid_details_return_reaction_metrics(data_pop):
   
    # Arrange
    post_id=1
    actual_reactions={'WOW':2,'LOVE':1,'SAD':1}
    
    # Act
    reactions_for_post=get_reaction_metrics(post_id)

    # Assert
    assert reactions_for_post [ReactionChoices.WOW.value] == actual_reactions [ReactionChoices.WOW.value]
    assert reactions_for_post[ReactionChoices.LOVE.value] == actual_reactions [ReactionChoices.LOVE.value]
    assert reactions_for_post[ReactionChoices.SAD.value] == actual_reactions [ReactionChoices.SAD.value]
    assert type(reactions_for_post) is dict
    
@pytest.mark.django_db
def test_get_reaction_metrics_when_invalid_post_id_raise_invalid_post_exception(data_pop):
    
    # Arrange
    post_id=0
    
    # Act
   
    # Assert
    with pytest.raises(InvalidPostException):
        assert get_reaction_metrics(post_id)
    
    
@pytest.mark.django_db
def test_get_reaction_metrics_when_post_id_has_no_metrics_return_empty_dict(data_pop):
    
    # Arrange
    empty_dict={}
    post_id=10
    
    # Act
    reactions_dict=get_reaction_metrics(post_id)

    # Assert
    assert reactions_dict == empty_dict
    
# Task - 9
# delete post

@pytest.mark.django_db
def test_delete_post_when_valid_details_given_delete_post(data_pop):
    
    # Arrange
    post_id=2
    user_id=1
    
    # Act
    delete_post(user_id, post_id)
    
    # Assert
    post_deleted=Post.objects.filter(posted_by_id=user_id,pk=post_id).exists()
    
    assert post_deleted is  False
          

@pytest.mark.django_db
def test_delete_post_when_invalid_user_id_raise_invalid_user_exception(data_pop):
    
    # Arrange
    post_id=1
    user_id=0
    
    # Act
    
    # Assert
    with pytest.raises(InvalidUserException):
        assert delete_post(user_id, post_id)
    
@pytest.mark.django_db
def test_delete_post_when_invalid_post_id_raise_invalid_post_exception(data_pop):
    
    # Arrange
    post_id=0
    user_id=1
    
    # Act
    
    # Assert
    with pytest.raises(InvalidPostException):
        assert delete_post(user_id, post_id)
    
  
@pytest.mark.django_db
@freeze_time("2012-01-14")
@pytest.mark.parametrize('post_id,user_id',[
    (1,3),(3,1),(9,1)
    ])
    
def test_delete_post_when_invalid_user_id_given_to_post_raise_user_cannot_delete_exception(data_pop,post_id,user_id):
    
    # Arrange
    user_id=user_id
    post_id=post_id
    
    # Act
        
    # Assert
    with pytest.raises(UserCannotDeletePostException):
        assert delete_post(user_id, post_id)
    
   
    
# Task - 10
# get post with more positive reactions

@pytest.mark.django_db
def test_get_post_with_more_positive_reactions_return_list_of_post_ids(data_pop):
    
    # Arrange
    expected_ids=[None,1,4,7]
    
    # Act
    posts=get_posts_with_more_positive_reactions()
    print(posts)
    # Assert
    assert type(posts) is list
    assert posts[-3] == expected_ids[-3]
    assert posts[-2] == expected_ids[-2]
    assert posts[-1] == expected_ids[-1]
    
    

# Task - 11
# get posts_reacted_by_user
@pytest.mark.django_db
def test_get_posts_reacted_by_user_when_valid_details_return_list_of_post_ids(data_pop):
    
    # Arrange
    user_id=4
    post_list=[7,8]

    # Act
    list_of_post_ids=get_posts_reacted_by_user(user_id)
    
    # Assert
    assert list_of_post_ids == post_list


@pytest.mark.django_db
def test_get_posts_reacted_by_user_when_invalid_user_id_raise_invalid_user_exception(data_pop):
   
    # Arrange
    user_id=0
    
    # Act
    
    # Assert
    with pytest.raises(InvalidUserException):
        assert get_posts_reacted_by_user(user_id)
    
    
# Task - 12    
# get reaction to post

@pytest.mark.django_db
def test_get_reactions_to_post_with_valid_details_return_list_of_dict_of_users_with_their_reaction(data_pop):
   
    # Arrange
    post_id=1
    actual_user_reaction_of_post= [
                                {
                                'user_id': 1, 'name': 'sulthan', 
                                'profile_pic': 'sulthan_babu/profile_pic', 
                                'reaction': 'WOW'
                                }, 
                                
                                {
                                'user_id': 5, 'name': 'che quevara', 
                                'profile_pic': 'chequeara/profile_pic', 
                                'reaction': 'WOW'
                                },
                                {
                                'user_id': 3, 'name': 'elon musk', 
                                'profile_pic': 'elonmusk/profile_pic',
                                'reaction': 'LOVE'
                                }, 
                                {
                                'user_id': 4, 'name': 'sravani',
                                'profile_pic': 'sravani/profile_pic', 
                                'reaction': 'SAD'
                                }
                     ]
        
    # Act
    list_of_dict_users_with_their_reaction=get_reactions_to_post(post_id)
    
    # Assert
    assert list_of_dict_users_with_their_reaction == actual_user_reaction_of_post
     
    
@pytest.mark.django_db
def test_reactions_to_post_when_invalid_post_id_raise_invalid_post_exception(data_pop):
   
    # Arrange
    post_id=0
    
    # Act
    
    # Assert
    with pytest.raises(InvalidPostException):
        assert get_reactions_to_post(post_id)
    


# get replies for comment  list_of_dict

@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_get_replies_for_comment_with_valid_details_return_list_of_dicts(data_pop):
    
    # Arrange
    comment_id=1
    actual_replies_list=[
                            {'comment_id': 4, 
                            'commenter': {
                                'user_id': 4, 
                                'name': 'sravani', 
                                'profile_pic': 'sravani/profile_pic'
                                },
                            'commented_at': '2012-01-14 00:00:00.000000', 
                            'comment_content': 'this is comment'
                                
                            },
                            
                            {
                            'comment_id': 5,
                            'commenter': {
                                'user_id': 5, 
                                'name': 'che quevara', 
                                'profile_pic': 'chequeara/profile_pic'
                                }, 
                            'commented_at': '2012-01-14 00:00:00.000000',
                            'comment_content': 'this is comment'
                                }
                ]
    
    #Act
    list_of_comment_replies=get_replies_for_comment(comment_id)
    
    # Assert
    assert list_of_comment_replies == actual_replies_list
    

@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_get_replies_for_comment_when_invalid_details_raise_invalid_comment_exception(data_pop):
    
    # Arrange
    comment_id= 0
    
    # Act
    
    # Assert
    with pytest.raises(InvalidCommentException):
        assert get_replies_for_comment(comment_id)
    




def function_to_compare_replies(dict1,dict2):
    
    function_to_compare_users(dict1['commenter'],dict2['commenter'])
    
    assert dict1["comment_id"] ==  dict2["comment_id"]
    assert dict1["commented_at"] ==  dict2["commented_at"]
    assert dict1["comment_content"] ==  dict2["comment_content"]
    
    assert dict1["reactions"]['count'] ==  dict2["reactions"]['count']
    assert dict1["reactions"]['type'].sort() ==  dict2["reactions"]['type'].sort()
     

def function_to_compare_comments(dict1,dict2):
    
    function_to_compare_users(dict1['commenter'],dict2['commenter'])
    
    assert dict1["comment_id"] ==  dict2["comment_id"]
    assert dict1["commented_at"] ==  dict2["commented_at"]
    assert dict1["comment_content"] ==  dict2["comment_content"]
    
    assert dict1["reactions"]['count'] ==  dict2["reactions"]['count']
    assert dict1["reactions"]['type'].sort() ==  dict2["reactions"]['type'].sort()
    assert dict1['replies_count'] == dict2['replies_count'] 
            
def function_to_compare_users(user1,user2):
    
    assert user1['user_id'] == user2['user_id']
    assert user1['name'] == user2['name']
    assert user1['profile_pic'] == user2['profile_pic']
    
def fucntion_to_compare_post_details(post1,post2):
    
    function_to_compare_users(post1['posted_by'],post2['posted_by'])
        
    assert post1['post_id'] == post2['post_id']
    assert post1['posted_at'] == post2['posted_at']
    assert post1['post_content'] == post2['post_content']
    assert post1['reactions']['count'] == post2['reactions']['count']
    assert post1['reactions']['type'].sort() == post2['reactions']['type'].sort()
    assert post1['comments_count'] == post2['comments_count']
      
    
    
    
# this is function is used for user_posts and get_posts
def function_used_to_compare(post,actual_post):
    
    if post and actual_post:
        for i in  range(len(post)):
            for j in range(len(post[i]['comments'])):
                for k in range(len(post[i]['comments'][j]['replies'])):
                    
                    dict1=post[i]['comments'][j]['replies'][k]
                    dict2=actual_post[i]['comments'][j]['replies'][k]
                    function_to_compare_replies(dict1,dict2)
                 
                dict1=post[i]['comments'][j]
                dict2=actual_post[i]['comments'][j]
                function_to_compare_comments(dict1,dict2)
            
            fucntion_to_compare_post_details(post[i],actual_post[i])
            
        return True
    else :
        return False

# Task - 13
# get_post

@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_get_post_with_valid_details_return_post_dict(data_pop):
   
    # Arrange
    post_id=1
    actual_post={
                   "post_id": 1,
                   "posted_by": {
                      "name": "sulthan",
                      "user_id": 1,
                      "profile_pic": "sulthan_babu/profile_pic"
                   },
                   "posted_at": "2012-01-14 00:00:00.000000",
                   "post_content": "empty",
                   "reactions": {
                      "count": 4,
                      "type": [
                         "LOVE",
                         "SAD",
                         "WOW"
                      ]
                   },
                   "comments": [
                      {
                         "comment_id": 1,
                         "commenter": {
                            "user_id": 3,
                            "name": "elon musk",
                            "profile_pic": "elonmusk/profile_pic"
                         },
                         "commented_at": "2012-01-14 00:00:00.000000",
                         "comment_content": "this is comment",
                         "reactions": {
                            "count": 4,
                            "type": [
                               "LOVE",
                               "SAD",
                               "WOW"
                            ]
                         },
                         "replies_count": 1,
                         "replies": [
                            {
                               "comment_id": 4,
                               "commenter": {
                                  "user_id": 4,
                                  "name": "sravani",
                                  "profile_pic": "sravani/profile_pic"
                               },
                               "commented_at": "2012-01-14 00:00:00.000000",
                               "comment_content": "this is comment",
                               "reactions": {
                                  "count": 1,
                                  "type": [
                                     "LIT"
                                  ]
                               }
                            }
                         ]
                      },
                      {
                         "comment_id": 2,
                         "commenter": {
                            "user_id": 1,
                            "name": "sulthan",
                            "profile_pic": "sulthan_babu/profile_pic"
                         },
                         "commented_at": "2012-01-14 00:00:00.000000",
                         "comment_content": "this is comment",
                         "reactions": {
                            "count": 1,
                            "type": [
                               "WOW"
                            ]
                         },
                         "replies_count": 1,
                         "replies": [
                            {
                               "comment_id": 3,
                               "commenter": {
                                  "user_id": 3,
                                  "name": "elon musk",
                                  "profile_pic": "elonmusk/profile_pic"
                               },
                               "commented_at": "2012-01-14 00:00:00.000000",
                               "comment_content": "this is comment",
                               "reactions": {
                                  "count": 1,
                                  "type": [
                                     "ANGRY"
                                  ]
                               }
                            }
                         ]
                      }
                   ],
                   "comments_count": 2
        }
    actual_post=[actual_post]
    
    # Act
    post=get_post(post_id)
    
    # Assert
    post=[post]
    output_is_true=function_used_to_compare(post,actual_post)
    
    assert  output_is_true is True
    

@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_get_post_when_invalid_post_id_given_raise_invalid_post_exception(data_pop):
   
    # Arrange
    post_id = 0
    
    # Act
    
    # Assert
    with pytest.raises(InvalidPostException):
        assert get_post(post_id)
   

# Task - 14
# get_user_posts

@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_get_user_posts_with_valid_details_return_list_of_post_dict(data_pop):
   
    # Arrange
    user_id=1
    actual_post=[
               {
                  "post_id": 1,
                  "posted_by": {
                     "name": "sulthan",
                     "user_id": 1,
                     "profile_pic": "sulthan_babu/profile_pic"
                  },
                  "posted_at": "2012-01-14 00:00:00.000000",
                  "post_content": "empty",
                  "reactions": {
                     "count": 4,
                     "type": [
                        "LOVE",
                        "SAD",
                        "WOW"
                     ]
                  },
                  "comments": [
                     {
                        "comment_id": 1,
                        "commenter": {
                           "user_id": 3,
                           "name": "elon musk",
                           "profile_pic": "elonmusk/profile_pic"
                        },
                        "commented_at": "2012-01-14 00:00:00.000000",
                        "comment_content": "this is comment",
                        "reactions": {
                           "count": 4,
                           "type": [
                              "LOVE",
                              "SAD",
                              "WOW"
                           ]
                        },
                        "replies_count": 1,
                        "replies": [
                           {
                              "comment_id": 4,
                              "commenter": {
                                 "user_id": 4,
                                 "name": "sravani",
                                 "profile_pic": "sravani/profile_pic"
                              },
                              "commented_at": "2012-01-14 00:00:00.000000",
                              "comment_content": "this is comment",
                              "reactions": {
                                 "count": 1,
                                 "type": [
                                    "LIT"
                                 ]
                              }
                           }
                        ]
                     },
                     {
                        "comment_id": 2,
                        "commenter": {
                           "user_id": 1,
                           "name": "sulthan",
                           "profile_pic": "sulthan_babu/profile_pic"
                        },
                        "commented_at": "2012-01-14 00:00:00.000000",
                        "comment_content": "this is comment",
                        "reactions": {
                           "count": 1,
                           "type": [
                              "WOW"
                           ]
                        },
                        "replies_count": 1,
                        "replies": [
                           {
                              "comment_id": 3,
                              "commenter": {
                                 "user_id": 3,
                                 "name": "elon musk",
                                 "profile_pic": "elonmusk/profile_pic"
                              },
                              "commented_at": "2012-01-14 00:00:00.000000",
                              "comment_content": "this is comment",
                              "reactions": {
                                 "count": 1,
                                 "type": [
                                    "ANGRY"
                                 ]
                              }
                           }
                        ]
                     }
                  ],
                  "comments_count": 2
               },
               {
                  "post_id": 2,
                  "posted_by": {
                     "name": "sulthan",
                     "user_id": 1,
                     "profile_pic": "sulthan_babu/profile_pic"
                  },
                  "posted_at": "2012-01-14 00:00:00.000000",
                  "post_content": "empty",
                  "reactions": {
                     "count": 1,
                     "type": [
                        "ANGRY"
                     ]
                  },
                  "comments": [
                     {
                        "comment_id": 8,
                        "commenter": {
                           "user_id": 5,
                           "name": "che quevara",
                           "profile_pic": "chequeara/profile_pic"
                        },
                        "commented_at": "2012-01-14 00:00:00.000000",
                        "comment_content": "this is comment",
                        "reactions": {
                           "count": 0,
                           "type": []
                        },
                        "replies_count": 1,
                        "replies": [
                           {
                              "comment_id": 9,
                              "commenter": {
                                 "user_id": 5,
                                 "name": "che quevara",
                                 "profile_pic": "chequeara/profile_pic"
                              },
                              "commented_at": "2012-01-14 00:00:00.000000",
                              "comment_content": "this is comment",
                              "reactions": {
                                 "count": 0,
                                 "type": []
                              }
                           }
                        ]
                     }
                  ],
                  "comments_count": 1
               },
               {
                  "post_id": 10,
                  "posted_by": {
                     "name": "sulthan",
                     "user_id": 1,
                     "profile_pic": "sulthan_babu/profile_pic"
                  },
                  "posted_at": "2012-01-14 00:00:00.000000",
                  "post_content": "empty",
                  "reactions": {
                     "count": 0,
                     "type": []
                  },
                  "comments": [],
                  "comments_count": 0
               }
            ]  
                
    # Act
    post=get_user_posts(user_id)    
    
    # Assert
    output_is_true=function_used_to_compare(post,actual_post)
    
    assert  output_is_true is True
    
    

@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_get_user_posts_when_invalid_user_id_raise_invalid_user_exception(data_pop):
    
    # Arrange
    user_id = 0
    
    # Act
    
    # Assert
    with pytest.raises(InvalidUserException):
         assert get_user_posts(user_id)    
   

