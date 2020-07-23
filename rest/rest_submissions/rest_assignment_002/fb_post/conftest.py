from freezegun import freeze_time
import datetime
import pytest
from fb_post.models import *
from fb_post.utils import *
from django.utils import timezone
from fb_post.constants import *
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
