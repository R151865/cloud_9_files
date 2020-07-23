from django.db.models import Prefetch
from fb_post.models import Post, Comment, User
from fb_post.exceptions import InvalidUserException
from .get_post import get_post_details_dict



def get_posts_query(user_id):
    post_list = Post.objects.select_related(
        'posted_by').prefetch_related(
            'reaction_set', Prefetch(
                'comment_set', queryset=Comment.objects.select_related(
                    'commented_by').prefetch_related(
                        'reaction_set'))).filter(posted_by_id=user_id)

    return post_list

#13
def get_user_posts(user_id=None):
    is_user_id_valid(user_id)
    
    check_user_id_valid(user_id)
    posts = get_posts_query(user_id)

    len(posts)
    posts_dict_list = []
    for post in posts:
        posts_dict_list.append(get_post_details_dict(post))

    return posts_dict_list
