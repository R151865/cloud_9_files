from .models import *
from .exceptions import *
from .constants import *
from datetime import *
from django.db.models import Count,Q
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
    user=User.objects.filter(pk=user_id).exists()
    post=Post.objects.filter(pk=post_id).exists()
    REACTION_CHOICES=['WOW','LIT','LOVE','HAHA','THUMBS-UP','THUMBS-DOWN','ANGRY','SAD']
 
    if user==False:
        raise InvalidUserException
    if post==False:
        raise InvalidPostException
        
    if reaction_type not in REACTION_CHOICES:
        raise InvalidReactionTypeException
    
    react=Reaction.objects.filter(post_id=post_id,reacted_by_id=user_id)
    len(react)
    
    if react.exists()==False:
        Reaction.objects.create(
                                post_id=post_id,
                                reacted_by_id=user_id,
                                reaction=reaction_type  
                                ) 
        
    elif react[0].reaction==reaction_type:
        react[0].delete()
    
    elif react[0].reaction!=reaction_type:
        react.update(
                    reaction=reaction_type,
                    reacted_at=datetime.now()
                    )
    
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
    #all exceptions
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


def reactions_numb_and_list(reactions):
    
    
    list_of_reactions=list(reactions.values_list('reaction',flat=True))
    count=len(list_of_reactions)
    list_of_reactions=list(set(list_of_reactions))
    return [count,list_of_reactions]

def comments_dictionary(comment):
    reactions=reactions_numb_and_list(comment.reaction_set.all())
    comment_details={
                                 "comment_id": comment.id,
                                 "commenter": {
                                                "user_id": comment.commented_by.id,
                                                "name": comment.commented_by.name,
                                                "profile_pic":comment.commented_by.profile_pic
                                              },
                                "commented_at":str(comment.commented_at),
                                "comment_content": comment.content,
                                "reactions": {
                                    "count": reactions[0],
                                    "type": reactions[1]
                                }
                                }
    return comment_details


#13
def get_post(post_id):
    
    #empty list for requered things and list
    #uniquer type for reactions
    if Post.objects.filter(pk=post_id).exists()==False:
        raise InvalidPostException
    
    comment_list=Comment.objects.select_related(
        'post__posted_by',
        'commented_by',
        'parent_comment__commented_by'
        ).filter(post_id=1).prefetch_related('reaction_set','post__reaction_set')
    post_dict=defaultdict(dict)
    for comment in comment_list:
        comment_dict=post_dict[comment.post]
        comment_dict[comment]=comment_dict.get(comment,[])
        post_dict[comment.post][comment].append(comment.parent_comment)
    
    list_of_post=[]
    for post,comments in post_dict.items():
        list_of_comments=[]
        for comment,replies in comments.items():
            
            reply_list=[]
            for reply in replies:
                if reply!=None:
                    reply_dictionary=comments_dictionary(reply)
                    reply_list.append(reply_dictionary)
                
            comment_dictionary=comments_dictionary(comment)
            
            comment_dictionary['replies_count']=len(reply_list)
            comment_dictionary['replies']=reply_list
            
            list_of_comments.append(comment_dictionary)
        
        reactions_of_post=reactions_numb_and_list(post.reaction_set.all())
        details_of_post={
                        "post_id": post.id,
                        "posted_by": {
                            "name": post.posted_by.name,
                            "user_id": post.posted_by.id,
                            "profile_pic": post.posted_by.profile_pic
                        },
                        "posted_at": str(post.posted_at),
                        "post_content": post.content,
                        "reactions": {
                            "count": reactions_of_post[0],
                            "type": reactions_of_post[1]
                        },
                        'comments':list_of_comments
                            
                        }
        return details_of_post
            
   
   
#14    
   
            
#15
def get_replies_for_comment(comment_id):
    #need to chanage comment_id
    if Comment.objects.filter(pk=1).exists()==False:
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
                        "commented_at": str(reply.commented_at),
                        "comment_content": reply.content
                    }
        replies_list.append(reply_dict)
    return replies_list
        
        
            
            
            
        
        