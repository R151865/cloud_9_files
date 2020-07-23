from django.db.models import Prefetch
from fb_post.models import Post, Comment
from .get_post_details_dict import get_post_details_dict
from .utils_validators import is_valid_user


# 13
def get_user_posts(user_id=None):

    is_valid_user(user_id)

    comment_queryset = Comment.objects.select_related('commented_by')\
                              .prefetch_related('reaction_set')

    post_objs = Post.objects\
                    .select_related('posted_by')\
                    .prefetch_related(
                        'reaction_set',
                        Prefetch('comment_set', queryset=comment_queryset)
                    ).filter(posted_by_id=user_id)#arrange properly

    user_posts_list = [
        get_post_details_dict(post_obj)
        for post_obj in post_objs
        ]

    return user_posts_list
