import pytest
from fb_post.exceptions import InvalidPostException
from fb_post.utils.get_reactions_to_post import get_reactions_to_post
from fb_post.constants import ConstantDicts
pytestmark = pytest.mark.django_db


# Task 12
# get reaction to post
@pytest.mark.django_db
def test_get_reactions_to_post_with_valid_details_return_list_of_dict_of_users_with_their_reaction(
        data_pop
):

    # Arrange
    post_id = 1
    actual_user_reaction_of_post = (
        ConstantDicts.original_user_reactions_of_post.value
        )

    # Act
    list_of_dict_users_with_their_reaction = get_reactions_to_post(post_id)

    # Assert
    assert list_of_dict_users_with_their_reaction == actual_user_reaction_of_post


@pytest.mark.django_db
def test_reactions_to_post_when_invalid_post_id_raise_invalid_post_exception(data_pop):

    # Arrange
    post_id = 0

    # Act
    with pytest.raises(InvalidPostException):
        get_reactions_to_post(post_id)
