from django.utils import timezone
import pytest
from freezegun import freeze_time
from fb_post.models import Comment
from fb_post.exceptions import (
    InvalidReplyContent,
    InvalidCommentException,
    InvalidUserException
    )
from fb_post.utils.reply_to_comment import reply_to_comment
pytestmark = pytest.mark.django_db


# Task - 4
# reply_to_comment
@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_reply_to_comment_when_comment_with_valid_details_create_reply_to_comment_and_return_reply_id(
        data_pop
):

    # Arrange
    comment_id = 8
    user_id = 1
    reply_content = 'this is reply content'
    comment = Comment.objects.get(pk=comment_id)

    # Act
    reply_id = reply_to_comment(user_id, comment_id, reply_content)

    # Assert
    reply = Comment.objects.get(pk=reply_id)

    assert reply.id == reply_id
    assert reply.commented_by_id == user_id
    assert reply.content == reply_content
    assert reply.commented_at == timezone.now()
    assert reply.parent_comment_id == comment_id
    assert comment.parent_comment_id is None


@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_reply_to_comment_for_reply_with_valid_details_return_new_reply_id(
        data_pop
):

    # Arrange
    parent_id = 1
    comment_id = 4
    user_id = 3
    reply_content = 'this is reply'

    parent_comment = Comment.objects.get(pk=parent_id)
    comment = Comment.objects.get(pk=comment_id)

    # Act
    reply_id = reply_to_comment(user_id, comment_id, reply_content)

    # Assert
    reply = Comment.objects.get(pk=reply_id)

    assert reply.id == reply_id
    assert reply.commented_by_id == user_id
    assert reply.content == reply_content
    assert reply.commented_at == timezone.now()
    assert reply.parent_comment_id == parent_comment.id
    assert comment.parent_comment_id == parent_comment.id
    assert parent_comment.parent_comment_id is  None


@pytest.mark.django_db
def test_reply_to_comment_when_invalid_user_id_raise_invalid_user_exception(
        data_pop
):

    # Arrage
    user_id = 0
    comment_id = 1
    reply_content = 'reply content'

    # Act
    with pytest.raises(InvalidUserException):
        reply_to_comment(user_id, comment_id, reply_content)


@pytest.mark.django_db
def test_reply_to_comment_when_invalid_comment_id_raise_invalid_comment_exception(
        data_pop
):

    # Arrage
    user_id = 1
    comment_id = 0
    reply_content = 'reply content'

    # Act
    with pytest.raises(InvalidCommentException):
        reply_to_comment(user_id, comment_id, reply_content)


@pytest.mark.django_db
def test_reply_to_comment_when_invalid_reply_content_raise_invalid_reply_content(
        data_pop
):

    # Arrage
    user_id = 1
    comment_id = 2
    reply_content = ""

    # Act
    with pytest.raises(InvalidReplyContent):
        reply_to_comment(user_id, comment_id, reply_content)
