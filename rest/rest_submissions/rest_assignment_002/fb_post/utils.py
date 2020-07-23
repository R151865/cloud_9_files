from .models import *
from .exceptions import *
from .constants import *
from datetime import *
from django.db.models import Count,Q,Prefetch
from collections import defaultdict

#2
def create_post(user_id, post_content):
    user=User.objects.filter(pk=user_id)
    if post_content=='':
        raise InvalidPostContent
    if user.exists():
            post=Post.objects.create(
                                    posted_by_id=user_id,
                                    content=post_content
                                    )
            return post.id
    else:
        raise InvalidUserException
        
#3
def create_comment(user_id, post_id, comment_content):
    user=User.objects.filter(pk=user_id)
    post=Post.objects.filter(pk=post_id)
    if comment_content=="":
        raise InvalidCommentContent
    if user.exists():
        if post.exists():
            comment=Comment.objects.create(
                                            content=comment_content,
                                            commented_by_id=user_id,
                                            post_id=post_id
                                            )
            return comment.id
        else:
            raise InvalidPostException
    else:
        raise InvalidUserException
    
#4
def reply_to_comment(user_id, comment_id, reply_content):
    comment=Comment.objects.filter(pk=comment_id)
    user=User.objects.filter(pk=user_id)
    len(comment)
    if reply_content=="":
        raise InvalidReplyContent
    
    if comment.exists():
        if user.exists():
            if comment[0].parent_comment_id==None:
                reply=Comment.objects.create(
                                            content=reply_content,
                                            commented_by_id=user_id,
                                            post_id=comment[0].post_id,
                                            parent_comment_id=comment_id
                                            )
            else:
                reply=Comment.objects.create(
                                            content=reply_content,
                                            commented_by_id=user_id,
                                            post_id=comment[0].post_id,
                                            parent_comment_id=comment[0].parent_comment_id
                                            )
            return reply.id
        else:
            raise InvalidUserException
    else:
        raise InvalidCommentException
    

#5
def react_to_post(user_id, post_id, reaction_type):
    REACTION_CHOICES=['WOW','LIT','LOVE',
                      'HAHA','THUMBS-UP',
                      'THUMBS-DOWN','ANGRY','SAD']
                    
    if User.objects.filter(pk=user_id).exists()==False:
        raise InvalidUserException
    if Post.objects.filter(pk=post_id).exists()==False:
        raise InvalidPostException
    if reaction_type.upper() not in REACTION_CHOICES:
        raise InvalidReactionTypeException
        
    reaction=Reaction.objects.filter(post_id=post_id,reacted_by_id=user_id)
    len(reaction)
    if reaction.exists()==False:
        Reaction.objects.create(
                                post_id=post_id,
                                reacted_by_id=user_id,
                                reaction=reaction_type
                                )
    
    elif reaction[0].reaction!=reaction_type:
        reaction.update(
                                reaction=reaction_type,
                                reacted_at=datetime.now()
                                )
    
    elif reaction[0].reaction==reaction_type:
        reaction[0].delete()

   
#6

def react_to_comment(user_id, comment_id, reaction_type):
    REACTION_CHOICES=['WOW','LIT','LOVE',
                      'HAHA','THUMBS-UP',
                      'THUMBS-DOWN','ANGRY','SAD']
                    
    if User.objects.filter(pk=user_id).exists()==False:
        raise InvalidUserException
    if Comment.objects.filter(pk=comment_id).exists()==False:
        raise InvalidCommentException
    if reaction_type.upper() not in REACTION_CHOICES:
        raise InvalidReactionTypeException
        
    reaction=Reaction.objects.filter(comment_id=comment_id,reacted_by_id=user_id)
    len(reaction)
    if reaction.exists()==False:
        Reaction.objects.create(
                                comment_id=comment_id,
                                reacted_by_id=user_id,
                                reaction=reaction_type
                                )

    elif reaction[0].reaction!=reaction_type:
        reaction.update(
                                reaction=reaction_type,
                                reacted_at=datetime.now()
                                )

    elif reaction[0].reaction==reaction_type:
        reaction[0].delete()

    
#7
def get_total_reaction_count():
    return Reaction.objects.aggregate(count=Count('reacted_by'))

#8
def get_reaction_metrics(post_id):
    if Post.objects.filter(pk=post_id).exists()==False:
        raise InvalidPostException 
    
    reaction_list=Reaction.objects.filter(post_id=post_id).values_list('reaction').annotate(count=Count('reaction'))
    react_dict={}
    for react in reaction_list:
        react_dict[react[0]]=react[1]
    return react_dict  

#9
def delete_post(user_id, post_id):
    user=User.objects.filter(pk=user_id).exists()
    post=Post.objects.filter(pk=post_id)
    len(post)
    if user==False:
        raise InvalidUserException
    if post.exists()==False:
        raise InvalidPostException
    if post[0].posted_by_id!=user_id:
        raise UserCannotDeletePostException
    post[0].delete()
    
#10
def get_posts_with_more_positive_reactions():
    num_positive=Count('reaction',filter=Q(reaction__in=['WOW','LIT','LOVE','HAHA','THUMBS-UP']))
    num_negative=Count('reaction',filter=Q(reaction__in=['THUMBS-DOWN','ANGRY','SAD']))
    
    return list(Reaction.objects.select_related('post').values('post_id').annotate(
        num_positive=num_positive,
        num_negative=num_negative
        ).filter(num_positive__gt=num_negative).values_list('post_id',flat=True))
    
#11
def get_posts_reacted_by_user(user_id):
    if User.objects.filter(pk=user_id).exists()==False:
        raise InvalidUserException
    return list(Post.objects.filter(posted_by_id=user_id).values_list('id',flat=True))
    
#12
def get_reactions_to_post(post_id):
    if Post.objects.filter(pk=post_id).exists()==False:
        raise InvalidPostException
        
    reactors=Reaction.objects.filter(post_id=post_id).select_related('reacted_by')
    post_reactions=[]
    for react in reactors:
        user_dict= {
                    'user_id':react.reacted_by.id,
                    'name':react.reacted_by.name,
                    'profile_pic':react.reacted_by.profile_pic,
                    'reaction':react.reaction
                    }
        post_reactions.append(user_dict)
    return post_reactions 


#related to task 13
def get_reaction_data_for_reactions_list(reactions_list):
    diff_reactions_list=[]
    for reaction in reactions_list:
        diff_reactions_list.append(reaction.reaction)
        
    count=len(diff_reactions_list)
    reaction_type=list(set(diff_reactions_list))
    output={
                'count':count,
                'reactions_type':reaction_type
                }
    return output


#related to task 13
def get_comment_or_reply_dict(comment):
    reactions=get_reaction_data_for_reactions_list(list(comment.reaction_set.all()))
    comment_dict={
                "comment_id": comment.id,
                "commenter": {
                                "user_id": comment.commented_by.id,
                                "name":comment.commented_by.name,
                                "profile_pic": comment.commented_by.profile_pic
                            },
                "commented_at":comment.commented_at.strftime('%Y-%m-%d %H:%M:%S.%f'),
                "comment_content":comment.content,
                "reactions": {
                                "count": reactions['count'],
                                "type": reactions['reactions_type']
                            }
                 }
                
    return comment_dict
#related to task 13
def get_details_of_post(post):
    reactions=get_reaction_data_for_reactions_list(list(post.reaction_set.all()))
    post_details= {  
                    "post_id": post.id,
                    "posted_by": {
                                    "name": post.posted_by.name,
                                    "user_id": post.posted_by.id,
                                    "profile_pic": post.posted_by.profile_pic
                                },
                    "posted_at": post.posted_at.strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "post_content":post.content,
                    "reactions": {
                                    "count": reactions['count'],
                                    "type": reactions['reactions_type']
                                }
                    
                    }

    return post_details
#13
def get_post(post_id=None,list_of_posts_for_user_id=False):
    #need to change the to_attr name
    if list_of_posts_for_user_id:
        # user_id in the name of post_id 
        user_id=post_id
        if User.objects.filter(pk=user_id).exists()==False:
            raise InvalidUserException
        
        post_data=Post.objects.select_related('posted_by').prefetch_related('reaction_set',
            Prefetch('comment_set',queryset=Comment.objects.select_related('commented_by').prefetch_related(
            'reaction_set'))).filter(posted_by_id=user_id)
    else:
        if Post.objects.filter(pk=post_id).exists()==False:
            raise InvalidPostException
        
        post_data=Post.objects.select_related('posted_by').prefetch_related('reaction_set',
            Prefetch('comment_set',queryset=Comment.objects.select_related('commented_by').prefetch_related(
            'reaction_set'))).filter(pk=post_id)
            
    len(post_data)
    list_of_posts=[]
    for post in post_data:
        post_comments=post.comment_set.all()
        
        comment_with_replies=defaultdict(list)
        for comment in post_comments:
            if comment.parent_comment_id==None:
                # this one line took one and half day time to debug(below one)
                comment_with_replies[comment]
                for reply in post_comments:
                    if reply.parent_comment_id==comment.id:
                        comment_with_replies[comment].append(reply)        
        print(comment_with_replies)
        comments_with_all_data=[]
        for comment,replies in comment_with_replies.items():
            list_of_replies=[]
            for reply in replies:
                list_of_replies.append(get_comment_or_reply_dict(reply))
                
            comment_data=get_comment_or_reply_dict(comment)
            comment_data['replies_count']=len(list_of_replies)
            comment_data['replies']=list_of_replies
            
            comments_with_all_data.append(comment_data)
    
        
        post_details=get_details_of_post(post)
        post_details['comments']=comments_with_all_data
        post_details['comments_count']=len(comments_with_all_data)
        
        list_of_posts.append(post_details)
    
    
    if list_of_posts_for_user_id:
        return list_of_posts
    else:
        return list_of_posts[0]

#14    
def get_user_posts(user_id):
    return get_post(user_id,list_of_posts_for_user_id=True)
    
#15
def get_replies_for_comment(comment_id):
    if Comment.objects.filter(pk=comment_id).exists()==False:
        raise InvalidCommentException
    replies=Comment.objects.filter(parent_comment_id=comment_id).select_related('commented_by')
    
    replies_list=[]
    for reply in replies:
        reply_dict={
                        "comment_id": reply.id,
                        "commenter": {
                                        "user_id": reply.commented_by.id,
                                        "name": reply.commented_by.name,
                                        "profile_pic":reply.commented_by.profile_pic
                                    },
                        "commented_at":reply.commented_at.strftime('%Y-%m-%d %H:%M:%S.%f'),
                        "comment_content": reply.content
                    }
        replies_list.append(reply_dict)
    return replies_list
        
        
            
            
            
        
        