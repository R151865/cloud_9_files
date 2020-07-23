from django.utils import timezone
import pytest
from freezegun import freeze_time
from fb_post.utils.create_post import create_post
from fb_post.models import Post, User
from fb_post.exceptions import InvalidUserException, InvalidPostContent
pytestmark = pytest.mark.django_db


# Task - 2
@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_create_post_with_valid_details_return_post_id(data_pop):

    # Arrange
    user_id = 1
    post_content = 'This is john cena content'

    # Act
    post_id = create_post(user_id, post_content)

    # Assert
    post = Post.objects.get(pk=post_id)

    assert post.id == post_id
    assert post.posted_by_id == user_id
    assert post.content == post_content
    assert post.posted_at == timezone.now()


def test_create_post_when_invalid_user_id_raise_invalid_user_exception():

    # Arrange
    user_id = 0
    post_content = 'this is post_content'

    # Act
    with pytest.raises(InvalidUserException):
        create_post(user_id, post_content)


def test_create_post_when_invalid_post_content_raise_invalid_post_content(data_pop):

    # Arrange
    user_id = 1
    post_content = ''

    # Act
    with pytest.raises(InvalidPostContent):
        create_post(user_id, post_content)
