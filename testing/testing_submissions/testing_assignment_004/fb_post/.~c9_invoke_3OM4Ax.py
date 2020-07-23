from django.test import TestCase

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






    










 

from freezegun import freeze_time
import datetime

import pytest
from .models import *
from  .utils import *
from django.utils import timezone

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
        {'posted_by_id':2, 'content':'empty'},
        {'posted_by_id':2, 'content':'empty'},
        {'posted_by_id':3, 'content':'empty'},
        {'posted_by_id':3, 'content':'empty'},
        {'posted_by_id':4, 'content':'empty'},
        {'posted_by_id':4, 'content':'empty'},
        {'posted_by_id':5, 'content':'empty'},
        {'posted_by_id':2, 'content':'empty'}
    
    ]

comments_list=[
        {'commented_by_id':3,'post_id':1,'content':'this is comment','parent_comment_id':None},
        {'commented_by_id':1,'post_id':1,'content':'this is comment','parent_comment_id':None},
        {'commented_by_id':3,'post_id':1,'content':'this is comment','parent_comment_id':2},
        {'commented_by_id':4,'post_id':1,'content':'this is comment','parent_comment_id':1},
        {'commented_by_id':5,'post_id':3,'content':'this is comment','parent_comment_id':None},
        {'commented_by_id':2,'post_id':3,'content':'this is comment','parent_comment_id':None},
        {'commented_by_id':3,'post_id':4,'content':'this is comment','parent_comment_id':5},
        {'commented_by_id':5,'post_id':4,'content':'this is comment','parent_comment_id':None}
        
    ]
reactions_list=[
    {'reacted_by_id':1,'post_id':1,'comment_id':None,'reaction':'WOW'},
    {'reacted_by_id':5,'post_id':1,'comment_id':None,'reaction':'WOW'},
    {'reacted_by_id':3,'post_id':1,'comment_id':None,'reaction':'LOVE'},
    {'reacted_by_id':4,'post_id':1,'comment_id':None,'reaction':'SAD'},
    
    {'reacted_by_id':3,'post_id':2,'comment_id':None,'reaction':'WOW'},
    {'reacted_by_id':4,'post_id':3,'comment_id':None,'reaction':'WOW'},
    {'reacted_by_id':5,'post_id':4,'comment_id':None,'reaction':'WOW'},
    
    
    {'reacted_by_id':1,'post_id':None,'comment_id':1,'reaction':'WOW'},
    {'reacted_by_id':5,'post_id':None,'comment_id':1,'reaction':'LOVE'},
    {'reacted_by_id':3,'post_id':None,'comment_id':1,'reaction':'LOVE'},
    {'reacted_by_id':4,'post_id':None,'comment_id':1,'reaction':'SAD'},
    
    {'reacted_by_id':3,'post_id':None,'comment_id':2,'reaction':'WOW'},
    {'reacted_by_id':4,'post_id':None,'comment_id':3,'reaction':'ANGRY'},
    {'reacted_by_id':5,'post_id':None,'comment_id':4,'reaction':'LIT'},
    
    ]






@pytest.fixture
def data_pop():
    
    user_bulk_list=[]
    for user in users_list:
        user_bulk_list.append(
            User(
            name=user['name'],
            profile_pic=user['profile_pic'] 
        )
        )
    user_objs=User.objects.bulk_create(user_bulk_list)
    
    post_bulk_list=[]    
    for post in posts_list:
        post_bulk_list.append(
            Post(
            posted_by_id=post['posted_by_id'],
            content=post['content'] 
        )
        )
    post_objs=Post.objects.bulk_create(post_bulk_list)
    
    
    comment_bulk_list=[]
    for comment in comments_list:
        comment_bulk_list.append(
            Comment(
            commented_by_id=comment['commented_by_id'],
            content=comment['content'] ,
            post_id=comment['post_id'],
            parent_comment_id =comment['parent_comment_id']
        )
        )
    comment_objs=Comment.objects.bulk_create(comment_bulk_list)
    
    
    reaction_bulk_list=[]
    for reaction in reactions_list:
        reaction_bulk_list.append(
            Reaction(
            reacted_by_id=reaction['reacted_by_id'],
            post_id=reaction['post_id'],
            comment_id=reaction['comment_id'],
            reaction=reaction['reaction']
        )
        )
    
    reaction_obj=Reaction.objects.bulk_create(reaction_bulk_list)
    
    dict_data={
        'user_objs':user_objs,
        'post_objs':post_objs,
        'comment_objs':comm
        
    }
    
    return user_objs
    

def test_1(data_pop):
    pass













@pytest.fixture
def user():
    name='john cena'
    profile_pic = 'john_cena/profile_pic'
    user_obj=User.objects.create(
                                name=name,
                                profile_pic=profile_pic
                                )
    
    return user_obj

@pytest.fixture
def post():
    
    name='under taker'
    profile_pic = 'under_taker/profile_pic'
    user =User.objects.create(
                                name=name,
                                profile_pic=profile_pic
                                )
    
    post_content='john cena post content'
    user_id=user.id
    post_obj=Post.objects.create(
                                posted_by_id=user_id,
                                content =post_content
                                )
    return post_obj 
    
@pytest.fixture
def comment(post):
    post_id=post.id
    comment_content='this is comment_content'
    
    name='rock'
    profile_pic = 'rock/profile_pic'
    user=User.objects.create(
                                name=name,
                                profile_pic=profile_pic
                                )
    
    comment_obj=Comment.objects.create(
                                    content=comment_content,
                                    post_id=post_id,
                                    commented_by_id=user.id
                                    )
    return comment_obj
    


invalid_user_exception= InvalidUserException
invalid_post_exception= InvalidPostException
invalid_comment_exception =InvalidCommentException
invalid_post_content_exception =InvalidPostContent
invalid_comment_content_exception =InvalidCommentContent



@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_create_post_with_valid_details(user):
    
    # Arrange
    user_id=user.id
    post_content= 'This is john cena content'    
    
    # Act
    post_id = create_post(user_id, post_content)
    post=Post.objects.get(pk=post_id)
    
    # Assert
    assert post.id == post_id
    assert post.posted_by_id == user_id
    assert post.content == post_content
    assert post.posted_at == timezone.now()


def test_create_post_when_invalid_user_id_given_raise_invaliduserexception(user):
    # Arrange
    user_id=2
    post_content ='this is post_content'
    
    # Act
    
    # Assert
    with pytest.raises(InvalidUserException):
        assert create_post(user_id, post_content)
   
def test_create_post_when_invalid_post_content_given_raise_invaliduserexception(user):
    # Arrange
    user_id=user.id 
    post_content =''
    error_type= InvalidPostContent
    # Act
    with pytest.raises(Exception) as error :
        create_post(user_id, post_content)
    
    # Assert
    assert error.type ==  error_type




@pytest.mark.django_db
@freeze_time("2012-01-14")
class Test_create_comment:
    
    def test_create_comment_with_valid_details(self,post,user):
        # Arrange
        post_id=post.id
        user_id=user.id
        comment_content='this is comment content'
        
        # Act
        comment_id=create_comment(user_id, post_id, comment_content)
        comment = Comment.objects.get(pk = comment_id)
       
        # Assert
        assert comment.id == comment_id
        assert comment.content ==  comment_content
        assert comment.post_id ==  post_id
        assert comment.commented_by_id ==  user_id
        assert comment.commented_at ==  timezone.now()
        
    def test_create_comment_when_invalid_user_id_raise_invaliduserexception(self,post):
        # Arrange
        user_id = 2
        post_id=post.id
        comment_content='this is comment content'
        error_type= InvalidUserException
        
        # Act
        with pytest.raises(Exception) as error :
            create_comment(user_id, post_id, comment_content)
    
        # Assert
        assert error.type ==  error_type
    
    def test_create_comment_when_invalid_post_id_raise_invalidpostexception(self,user):
        # Arrange
        user_id = user.id
        post_id=2
        comment_content='this is comment content'
        error_type= InvalidPostException
        
        # Act
        with pytest.raises(Exception) as error :
            create_comment(user_id, post_id, comment_content)
    
        # Assert
        assert error.type ==  error_type
        
    def test_create_comment_when_invalid_comment_content_raise_invalidcommentcontent(self,user,post):
        # Arrange
        user_id = user.id
        post_id=post.id
        comment_content=''
        error_type= InvalidCommentContent
        
        # Act
        with pytest.raises(Exception) as error :
            create_comment(user_id, post_id, comment_content)
    
        # Assert
        assert error.type ==  error_type

        

# reply_to_comment

#1.test reply to comment with valid data
# 2. test reply to comment in valid data raise error()
#3 .test reply to comment reply comment is == empty only
# test reply to comment when comment has parent comment id
# test reply to comment when when parent has no comment id


@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_reply_to_comment_when_comment_has_no_parent_comment_id_and_with_valid_details_reply_to_comment(comment,user):
     # Arrange
     comment_id=comment.id
     user_id=user.id
     reply_content='this is reply content'
     comment_has_no_parent_id = None
     created_date_and_time =timezone.now()
     
     # Act
     reply_id=reply_to_comment(user_id, comment_id, reply_content)
     reply=Comment.objects.get(pk=reply_id)
     
     # Assert
     assert reply.id ==  reply_id
     assert reply.commented_by_id == user_id
     assert reply.content == reply_content
     assert reply.commented_at == created_date_and_time
     assert reply.parent_comment_id == comment_id
     assert comment.parent_comment_id == comment_has_no_parent_id
     
     
@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_reply_to_comment_when_comment_has_parent_comment_id_and_with_valid_details_reply_to_parent_comment(comment,post,user):
     # Arrange
     user_id=user.id
     name='under taker'
     profile_pic = 'under_taker/profile_pic'
     comment_by=User.objects.create(
                                name=name,
                                profile_pic=profile_pic
                                )
                                
     post_id=post.id
     comment_content = 'this is comment content '                           
     parent_comment=Comment.objects.create(
                                    content=comment_content,
                                    post_id=post_id,
                                    commented_by_id=comment_by.id
                                    )
    
     comment=Comment.objects.create(
                                    content=comment_content,
                                    post_id=post_id,
                                    commented_by_id=comment_by.id,
                                    parent_comment_id = parent_comment.id
                                    )
     comment_id=comment.id
     reply_content='this is reply'
     parant_comment_has_parent_comment_id_none =None
     created_date_and_time =timezone.now()
     
     
     # Act
     reply_id=reply_to_comment(user_id, comment_id, reply_content)
     reply=Comment.objects.get(pk=reply_id)
     
     # Assert
     assert reply.id ==  reply_id
     assert reply.commented_by_id == user_id
     assert reply.content == reply_content
     assert reply.commented_at == created_date_and_time
     assert reply.parent_comment_id == parent_comment.id
     assert comment.parent_comment_id == parent_comment.id
     assert parent_comment.parent_comment_id == parant_comment_has_parent_comment_id_none
     
@pytest.mark.django_db
def test_reply_to_comment_when_invalid_user_id_raise_invaliduserexception(comment):
    # Arrage
    user_id = 5
    comment_id=comment.id
    reply_content ='reply content'
    error_type= InvalidUserException
        
    # Act
    with pytest.raises(Exception) as error:
        reply_to_comment(user_id, comment_id, reply_content)
     
        
    
    # Assert
    assert error.type == error_type

@pytest.mark.django_db
def test_reply_to_comment_when_invalid_comment_id_raise_invalidcommentexception(user):
    # Arrage
    user_id = user.id
    comment_id=1
    reply_content ='reply content'
    error_type= InvalidCommentException
        
    # Act
    with pytest.raises(Exception) as error:
        reply_to_comment(user_id, comment_id, reply_content)
     
        
    
    # Assert
    assert error.type == error_type

@pytest.mark.django_db
def test_reply_to_comment_when_invalid_reply_content_raise_invalidcommentexception(user,comment):
    # Arrage
    user_id = user.id
    comment_id=comment.id
    reply_content =""
    error_type= InvalidReplyContent
        
    # Act
    with pytest.raises(Exception) as error:
        reply_to_comment(user_id, comment_id, reply_content)
     
        
    
    # Assert
    assert error.type == error_type
    




#react to post

@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_react_to_post_with_valild_details_give_reaction_to_post(post,user):
    # Arrange
    post_id=post.id
    user_id=user.id
    reaction_type='WOW'
    reacted_time_to_post = timezone.now()
    
    # Act
    react_to_post(user_id, post_id, reaction_type)
    reaction=Reaction.objects.all().last()
    
    # Assert
    assert reaction.reaction == reaction_type
    assert reaction.post_id == post_id
    assert reaction.reacted_by_id  == user_id
    assert reaction.reacted_at == reacted_time_to_post


@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_react_to_post_update_reaction_type_when_different_reaction_type_given_by_same_user(post,user):
    # Arrange
    post_id=post.id
    user_id=user.id
    reaction_type='LOVE'
    updated_reaction_type ='ANGRY'
    react_to_post(user_id, post_id, reaction_type)
    updated_reacted_time_to_post = timezone.now()
    
    
    # Act
    react_to_post(user_id, post_id, updated_reaction_type)
    reaction=Reaction.objects.all().last()
    
    # Assert
    assert reaction.reaction == updated_reaction_type
    assert reaction.post_id == post_id
    assert reaction.reacted_by_id  == user_id
    assert reaction.reacted_at == updated_reacted_time_to_post
    

@pytest.mark.django_db
def test_react_to_post_delete_reaction_type_when_same_reaction_type_given_by_same_user(post,user):
    # Arrange
    post_id=post.id
    user_id=user.id
    reaction_type='LOVE'
    same_reaction_type='LOVE'
    react_to_post(user_id, post_id, reaction_type)
    is_false =False
    
    # Act
    react_to_post(user_id, post_id, same_reaction_type)
    deleted_reaction_return_false=Reaction.objects.filter(reacted_by_id=user_id,
                                                        post_id=post_id,
                                                        reaction= reaction_type).exists()
    # Assert
    assert deleted_reaction_return_false == is_false

@pytest.mark.django_db
def test_react_to_post_when_invalid_user_id_raise_invaliduserexception(post):
    # Arrange
    post_id=post.id
    user_id=2
    reaction_type='LOVE'
    
    # Act
    with pytest.raises(Exception) as error:
        react_to_post(user_id, post_id, reaction_type)
    
    # Assert
    assert error.type == invalid_user_exception
    

@pytest.mark.django_db
def test_react_to_post_when_invalid_post_id_raise_invalidpostexception(user):
    # Arrange
    post_id=2
    user_id=user.id
    reaction_type='LOVE'
    
    # Act
    with pytest.raises(Exception) as error:
        react_to_post(user_id, post_id, reaction_type)
    
    # Assert
    assert error.type == invalid_post_exception
    

@pytest.mark.django_db
def test_react_to_post_when_invalid_reaction_type_raise_invalidreactiontype(user,post):
    # Arrange
    post_id=post.id
    user_id=user.id
    reaction_type='Testing_cases'
    invalid_reaction_type_content= InvalidReactionTypeException
    # Act
    with pytest.raises(Exception) as error:
        react_to_post(user_id, post_id, reaction_type)
    
    # Assert
    assert error.type == invalid_reaction_type_content
    


#react to comment

#1. test react to comment raise error when  user id ,post id , reaction type are in valid
#2.test react  to comment     with valid details 
#3.test react  to comment   if user reacting at first time
#4.test react to comment  update react when user react with different react type
#5.test react to comment   deleting the react when user reacting same react type
    
@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_react_to_comment_with_valild_details_give_reaction_to_post(comment,user):
    # Arrange
    comment_id=comment.id
    user_id=user.id
    reaction_type='LIT'
    reacted_time_to_post = timezone.now()
    
    # Act
    react_to_comment(user_id, comment_id, reaction_type)
    reaction=Reaction.objects.all().last()
    
    # Assert
    assert reaction.reaction == reaction_type
    assert reaction.comment_id == comment_id 
    assert reaction.reacted_by_id  == user_id
    assert reaction.reacted_at == reacted_time_to_post


@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_react_to_comment_update_reaction_type_when_different_reaction_type_given_by_same_user(comment,user):
    # Arrange
    comment_id=comment.id
    user_id=user.id
    reaction_type='LOVE'
    updated_reaction_type ='ANGRY'
    react_to_comment(user_id, comment_id, reaction_type)
    updated_reacted_time_to_post = timezone.now()
    
    
    # Act
    react_to_comment(user_id, comment_id, updated_reaction_type)
    reaction=Reaction.objects.all().last()
    
    # Assert
    assert reaction.reaction == updated_reaction_type
    assert reaction.comment_id == comment_id
    assert reaction.reacted_by_id  == user_id
    assert reaction.reacted_at == updated_reacted_time_to_post



@pytest.mark.django_db
def test_react_to_comment_delete_reaction_type_when_same_reaction_type_given_by_same_user(comment,user):
    # Arrange
    comment_id=comment.id
    user_id=user.id
    reaction_type='LOVE'
    same_reaction_type='LOVE'
    react_to_comment(user_id, comment_id, reaction_type)
    is_false =False
    
    # Act
    react_to_comment(user_id, comment_id, same_reaction_type)
    deleted_reaction_return_false=Reaction.objects.filter(reacted_by_id=user_id,
                                                        comment_id=comment_id,
                                                        reaction= reaction_type).exists()
    # Assert
    assert deleted_reaction_return_false == is_false

@pytest.mark.django_db
def test_react_to_comment_when_invalid_user_id_raise_invaliduserexception(comment):
    # Arrange
    comment_id=comment.id
    user_id=5
    reaction_type='LOVE'
    
    # Act
    with pytest.raises(Exception) as error:
        react_to_comment(user_id, comment_id, reaction_type)
    
    # Assert
    assert error.type == invalid_user_exception
    

@pytest.mark.django_db
def test_react_to_comment_when_invalid_post_id_raise_invalidpostexception(user):
    # Arrange
    comment_id=2
    user_id=user.id
    reaction_type='LOVE'
    
    # Act
    with pytest.raises(Exception) as error:
        react_to_comment(user_id, comment_id, reaction_type)
    
    # Assert
    assert error.type == invalid_comment_exception
    

@pytest.mark.django_db
def test_react_to_comment_when_invalid_reaction_type_raise_invalidreactiontype(user,comment):
    # Arrange
    comment_id=comment.id
    user_id=user.id
    reaction_type='Testing_cases'
    invalid_reaction_type_content= InvalidReactionTypeException
    # Act
    with pytest.raises(Exception) as error:
        react_to_comment(user_id, comment_id, reaction_type)
    
    # Assert
    assert error.type == invalid_reaction_type_content
