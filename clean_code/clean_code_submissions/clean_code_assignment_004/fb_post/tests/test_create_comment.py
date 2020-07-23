from django.utils import timezone
import pytest
from freezegun import freeze_time
from fb_post.utils.create_comment import create_comment
from fb_post.models import Comment, Post, User
from fb_post.exceptions import InvalidUserException, InvalidPostException
from fb_post.exceptions import InvalidCommentContent
pytestmark = pytest.mark.django_db


# Task - 3
@pytest.mark.django_db
@freeze_time("2012-01-14")
class TestCreateComment:

    def test_create_comment_with_valid_details_return_comment_id(
            self, data_pop):

        # Arrange
        post_id = 1
        user_id = 2
        comment_content = 'this is comment content'

        # Act
        comment_id = create_comment(user_id, post_id, comment_content)

        # Assert
        comment = Comment.objects.get(pk=comment_id)

        assert comment.id == comment_id
        assert comment.content == comment_content
        assert comment.post_id == post_id
        assert comment.commented_by_id == user_id
        assert comment.commented_at == timezone.now()


    def test_create_comment_when_invalid_user_id_raise_invalid_user_exception(
            self, data_pop):

        # Arrange
        user_id = 0
        post_id = 1
        comment_content = 'this is comment content'

        # Act
        with pytest.raises(InvalidUserException):
            create_comment(user_id, post_id, comment_content)


    def test_create_comment_when_invalid_post_id_raise_invalid_post_exception(
            self, data_pop):

        # Arrange
        user_id = 1
        post_id = 0
        comment_content = 'this is comment content'

        # Act
        with pytest.raises(InvalidPostException):
            create_comment(user_id, post_id, comment_content)


    def test_create_comment_when_invalid_comment_content_raise_invalid_comment_content(
            self, data_pop):

        # Arrange
        user_id = 1
        post_id = 2
        comment_content = ''

        # Act
        with pytest.raises(InvalidCommentContent):
            create_comment(user_id, post_id, comment_content)
