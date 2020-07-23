import pytest
from fb_post.utils.get_posts_with_more_positive_reactions import (
    get_posts_with_more_positive_reactions)

pytestmark = pytest.mark.django_db


# Task - 10
# get post with more positive reactions

@pytest.mark.django_db
def test_get_post_with_more_positive_reactions_return_list_of_post_ids(
        data_pop
):

    # Arrange
    expected_post_ids_list = [None, 1, 4, 7]

    # Act
    posts_ids_list = get_posts_with_more_positive_reactions()

    # Assert
    assert posts_ids_list == expected_post_ids_list
