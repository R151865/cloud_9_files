import pytest
from freezegun import freeze_time
from fb_post.constants import ConstantDicts
from fb_post.exceptions import InvalidCommentException
from fb_post.utils.get_replies_for_comment import get_replies_for_comment
pytestmark = pytest.mark.django_db


# get replies for comment  list_of_dict
@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_get_replies_for_comment_with_valid_details_return_list_of_dicts(
        data_pop
):

    # Arrange
    comment_id = 1
    actual_replies_list = ConstantDicts.original_replies_list_for_comment.value

    # Act
    list_of_comment_replies = get_replies_for_comment(comment_id)

    # Assert
    assert list_of_comment_replies == actual_replies_list


@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_get_replies_for_comment_when_invalid_details_raise_invalid_comment_exception(
        data_pop
):

    # Arrange
    comment_id = 0

    # Act
    with pytest.raises(InvalidCommentException):
        get_replies_for_comment(comment_id)
