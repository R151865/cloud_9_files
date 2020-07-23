import pytest
from freezegun import freeze_time
from fb_post.exceptions import UserCannotDeletePostException
from fb_post.models import Post
from fb_post.exceptions import (
    InvalidUserException,
    InvalidPostException
    )
from fb_post.utils.delete_post import delete_post

pytestmark = pytest.mark.django_db


# Task - 9
# delete post
@pytest.mark.django_db
def test_delete_post_when_valid_details_given_delete_post(data_pop):

    # Arrange
    post_id = 2
    user_id = 1

    # Act
    delete_post(user_id, post_id)

    # Assert
    is_post_exists_return_false = Post.objects\
                       .filter(
                           posted_by_id=user_id,
                           pk=post_id
                       ).exists()

    assert is_post_exists_return_false is  False


@pytest.mark.django_db
def test_delete_post_when_invalid_user_id_raise_invalid_user_exception(
        data_pop
):

    # Arrange
    post_id = 1
    user_id = 0

    # Act
    with pytest.raises(InvalidUserException):
        delete_post(user_id, post_id)


@pytest.mark.django_db
def test_delete_post_when_invalid_post_id_raise_invalid_post_exception(
        data_pop
):

    # Arrange
    post_id = 0
    user_id = 1

    # Act
    with pytest.raises(InvalidPostException):
        delete_post(user_id, post_id)


@pytest.mark.django_db
@freeze_time("2012-01-14")
@pytest.mark.parametrize('post_id, user_id', [
    (1, 3),
    (3, 1),
    (9, 1)
    ])

def test_delete_post_when_invalid_user_id_given_to_post_raise_user_cannot_delete_exception(
        data_pop,
        post_id,
        user_id
):

    # Assert
    with pytest.raises(UserCannotDeletePostException):
        delete_post(user_id, post_id)
