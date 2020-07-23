


def get_user_dict(user):

    return {
        "user_id": user.id,
        "name": user.name,
        "profile_pic": user.profile_pic
    }



def get_reaction_list(reactions_list):

    unique_reactions_list = []
    for reaction in reactions_list:
        unique_reactions_list.append(reaction.reaction)

    count = len(unique_reactions_list)
    reaction_type_list = list(set(unique_reactions_list))

    return {
        "count": count,
        "type": reaction_type_list
    }


def get_date_time(date_time):
    return date_time.strftime('%Y-%m-%d %H:%M:%S.%f') #TODO: keep that string in constants


def get_comment_dict(comment):

    reactions = get_reaction_list(list(comment.reaction_set.all()))
    comment_user_dict = get_user_dict(comment.commented_by)
    date_time = get_date_time(comment.commented_at)

    comment_dict = {
                "comment_id": comment.id,
                "commenter": comment_user_dict,
                "commented_at": date_time,
                "comment_content": comment.content,
                "reactions": reactions
    }

    return comment_dict


def get_post_dict(post):

    reactions = get_reaction_list(list(post.reaction_set.all()))
    post_user_dict = get_user_dict(post.posted_by)
    date_time = get_date_time(post.posted_at)

    post_dict = {
                "post_id": post.id,
                "posted_by": post_user_dict,
                "posted_at": date_time,
                "post_content": post.content,
                "reactions": reactions
    }

    return post_dict


"""
from dataclasses import dataclass

from typing import *

@dataclass
class UserDict:
    user_id: int
    name: str
    profile_pic: str



@dataclass
class CommentDict:
    comment_id: int
    commenter: Dict
    commented_at: str
    reactions: List


@dataclasses
class PostDict:
    post_id: int
    posted_by: str
    posted_at: str
    post_content: str
    reactions: List[str]

@dataclass
class ReactionsDict:
    count: int
    type: List[str]
"""

