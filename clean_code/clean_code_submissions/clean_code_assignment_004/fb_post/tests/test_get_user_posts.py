import pytest
from freezegun import freeze_time
from fb_post.constants import ConstantDicts
from fb_post.exceptions import InvalidUserException
from fb_post.utils.get_user_posts import get_user_posts
from .test_get_post import function_used_to_compare
pytestmark = pytest.mark.django_db


# Task - 14
# get_user_posts
@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_get_user_posts_with_valid_details_return_list_of_post_dict(data_pop):

    # Arrange
    user_id = 1
    user_original_posts_list = ConstantDicts.user_original_posts.value

    # Act
    post_list = get_user_posts(user_id)

    # Assert
    are_they_valid_posts = function_used_to_compare(
        post_list,
        user_original_posts_list
    )

    assert are_they_valid_posts is True


@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_get_user_posts_when_invalid_user_id_raise_invalid_user_exception(
        data_pop
):

    # Arrange
    user_id = 0

    # Act
    with pytest.raises(InvalidUserException):
        get_user_posts(user_id)
