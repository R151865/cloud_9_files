from collections import defaultdict
from django.db.models import Prefetch
from fb_post.models import Post, Comment
from fb_post.exceptions import InvalidPostException
from errors import is_post_id_valid
from dicts import get_comment_dict
"""
# related to task 13
def get_reaction_data_for_reactions_list(reactions_list):
    diff_reactions_list = []
    for reaction in reactions_list:
        diff_reactions_list.append(reaction.reaction)

    count = len(diff_reactions_list)
    reaction_type = list(set(diff_reactions_list))

    output = {
        'count':count,
        'reactions_type':reaction_type
        }
    return output
"""

# related to task 13

def get_comment_or_reply_dict(comment):

    reactions = get_reaction_data_for_reactions_list(
        list(comment.reaction_set.all()))
    comment_dict = {
                "comment_id": comment.id,
                "commenter": {
                    "user_id": comment.commented_by.id,
                    "name":comment.commented_by.name,
                    "profile_pic": comment.commented_by.profile_pic
                    },
                "commented_at": comment.commented_at.strftime(
                    '%Y-%m-%d %H:%M:%S.%f'),
                "comment_content": comment.content,
                "reactions": {
                    "count": reactions['count'],
                    "type": reactions['reactions_type']
                    }
    }

    return comment_dict


# related to task 13
def get_details_of_post(post):

    reactions = get_reaction_data_for_reactions_list(
        list(post.reaction_set.all()))
    post_details = {
                "post_id": post.id,
                "posted_by": {
                    "name": post.posted_by.name,
                    "user_id": post.posted_by.id,
                    "profile_pic": post.posted_by.profile_pic
                    },
                "posted_at": post.posted_at.strftime(
                    '%Y-%m-%d %H:%M:%S.%f'),
                "post_content": post.content,
                "reactions": {
                    "count": reactions['count'],
                    "type": reactions['reactions_type']
                    }
    }

    return post_details


def filter_comment_and_replies_dict(post):

    post_comments_list = post.comment_set.all()
    comment_with_replies_dict = defaultdict(list)

    for comment in post_comments_list:
        if comment.parent_comment_id is None:
         # this one line took one and half day time to debug(below one)
            comment_with_replies_dict[comment] = filter_replies_list(comment,post_comments_list)

    return comment_with_replies_dict


def filter_replies_list(comment, replies):
    comment_replies = []

    for reply in replies:
        if reply.parent_comment_id == comment.id:
            comment_replies.append(reply)

    return comment_replies


def get_replies_dict_list(replies):
    replies_dict_list= []
    for reply in replies:
        replies_dict_list.append(get_comment_or_reply_dict(reply))

    return replies_dict_list


def get_comment_in_dict_form(comment, list_of_replies):

    comment_data = get_comment_or_reply_dict(comment)
    comment_data['replies_count'] = len(list_of_replies)
    comment_data['replies'] = list_of_replies

    return comment_data


def get_comments_and_replies_all_full_data(comment_with_replies):

    comments_along_with_replies_list = []
    for comment, replies in comment_with_replies.items():

        list_of_replies = get_replies_dict_list(replies)
        comment_data = get_comment_in_dict_form(comment, list_of_replies)
        comments_along_with_replies_list.append(comment_data)

    return comments_along_with_replies_list


def prefetch_post_from_db(post_id):
    comment_query_set = Comment.objects.select_related('commented_by')\
                               .prefetch_related('reaction_set')
    
    posts = Post.objects.select_related('posted_by')\
               .prefetch_related(
                   'reaction_set',
                   Prefetch(
                       'comment_set',
                       queryset=comment_query_set)
               ).filter(pk=post_id)

    return posts


def get_post_dict_(post, comments_with_all_data):

    post_details = get_details_of_post(post)
    post_details['comments'] = comments_with_all_data
    post_details['comments_count'] = len(comments_with_all_data)

    return post_details


def get_post_dict(post):
    comment_with_replies_dict = filter_comment_and_replies_dict(post)

    comments_with_all_data = get_comments_and_replies_all_full_data(
        comment_with_replies_dict)
    post_dict = get_post_dict_(post, comments_with_all_data)

    return post_dict

# 13
def get_post(post_id=None):
    
    is_post_id_valid(post_id)
    posts = prefetch_post_from_db(post_id)

    len(posts)
    post = posts[0]
    return get_post_dict(post)
