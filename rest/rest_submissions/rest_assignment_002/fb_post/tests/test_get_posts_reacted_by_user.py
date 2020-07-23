import pytest
from fb_post.exceptions import (
    InvalidUserException
    )
from fb_post.utils.get_posts_reacted_by_user import get_posts_reacted_by_user
pytestmark = pytest.mark.django_db


# Task 11
# get posts_reacted_by_user
@pytest.mark.django_db
def test_get_posts_reacted_by_user_when_valid_details_return_list_of_post_ids(
        data_pop
):

    # Arrange
    user_id = 4
    post_list = [7, 8]

    # Act
    list_of_post_ids = get_posts_reacted_by_user(user_id)

    # Assert
    assert list_of_post_ids == post_list


@pytest.mark.django_db
def test_get_posts_reacted_by_user_when_invalid_user_id_raise_invalid_user_exception(
        data_pop
):

    # Arrange
    user_id = 0

    # Act
    with pytest.raises(InvalidUserException):
        get_posts_reacted_by_user(user_id)
