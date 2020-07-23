import pytest

from fb_post.constants import ReactionChoices
from fb_post.exceptions import (
    InvalidPostException
    )
from fb_post.utils.get_reaction_metrics import get_reaction_metrics

pytestmark = pytest.mark.django_db


# Task - 8   
# get reaction metrics
@pytest.mark.django_db
def test_get_reaction_metrics_with_valid_details_return_reaction_metrics(
        data_pop
):

    # Arrange
    post_id = 1
    actual_reactions_dict = {
        'WOW': 2,
        'LOVE': 1,
        'SAD': 1
    }

    # Act
    post_reactions_dict = get_reaction_metrics(post_id)

    # Assert
    assert post_reactions_dict[ReactionChoices.WOW.value] == actual_reactions_dict[ReactionChoices.WOW.value]
    assert post_reactions_dict[ReactionChoices.LOVE.value] == actual_reactions_dict[ReactionChoices.LOVE.value]
    assert post_reactions_dict[ReactionChoices.SAD.value] == actual_reactions_dict[ReactionChoices.SAD.value]
    assert type(post_reactions_dict) == dict


@pytest.mark.django_db
def test_get_reaction_metrics_when_invalid_post_id_raise_invalid_post_exception(
        data_pop
):

    # Arrange
    post_id = 0

    # Act
    with pytest.raises(InvalidPostException):
        get_reaction_metrics(post_id)


@pytest.mark.django_db
def test_get_reaction_metrics_when_post_id_has_no_metrics_return_empty_dict(
        data_pop
):

    # Arrange
    empty_reactions_dict = {}
    post_id = 10

    # Act
    post_reactions_dict = get_reaction_metrics(post_id)

    # Assert
    assert post_reactions_dict == empty_reactions_dict
