from fb_post.models import Comment
from .utils_validators import (
    is_comment_content_valid,
    is_user_id_valid,
    is_post_id_valid
)


#3
def create_comment(user_id, post_id, comment_content):

    is_comment_content_valid(comment_content)
    is_user_id_valid(user_id)
    is_post_id_valid(post_id) #TODO: is_valid_post_id

    comment = Comment.objects.create(content=comment_content,
                                     post_id=post_id,
                                     commented_by_id=user_id)

    return comment.id
