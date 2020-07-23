from django.utils import timezone
import pytest
from freezegun import freeze_time
from fb_post.models import Reaction
from fb_post.constants import ReactionChoices
from fb_post.exceptions import (
    InvalidReactionTypeException,
    InvalidPostException,
    InvalidUserException
    )
from fb_post.utils.react_to_post import react_to_post
pytestmark = pytest.mark.django_db


# Task - 5
# react to post
@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_react_to_post_with_valild_details_react_to_post(data_pop):

    # Arrange
    post_id = 9
    user_id = 1
    reaction_type = ReactionChoices.WOW.value

    # Act
    react_to_post(user_id, post_id, reaction_type)

    # Assert
    reaction = Reaction.objects.all().last()

    assert reaction.reaction == reaction_type
    assert reaction.post_id == post_id
    assert reaction.reacted_by_id == user_id
    assert reaction.reacted_at == timezone.now()


@pytest.mark.django_db
@freeze_time("2012-01-14")
@pytest.mark.parametrize('reaction_type, updated_reaction_type', [
    (ReactionChoices.LIT.value, ReactionChoices.THUMBS_DOWN.value),
    (ReactionChoices.THUMBS_DOWN.value, ReactionChoices.LIT.value),
    (ReactionChoices.ANGRY.value, ReactionChoices.SAD.value)
    ])
def test_react_to_post_when_different_reaction_type_given_by_same_user_update_reaction(
        data_pop,
        updated_reaction_type,
        reaction_type
):

    # Arrange
    post_id = 10
    user_id = 6
    react_to_post(user_id, post_id, reaction_type)

    # Act
    react_to_post(user_id, post_id, updated_reaction_type)

    # Assert
    reaction = Reaction.objects.all().last()

    assert reaction.reaction == updated_reaction_type
    assert reaction.post_id == post_id
    assert reaction.reacted_by_id == user_id
    assert reaction.reacted_at == timezone.now()


@pytest.mark.django_db
def test_react_to_post_when_same_reactions_given_by_same_user_delete_reaction(
        data_pop
):

    # Arrange
    post_id = 10
    user_id = 6
    reaction_type = ReactionChoices.LOVE.value
    same_reaction_type = ReactionChoices.LOVE.value
    react_to_post(user_id, post_id, reaction_type)

    # Act
    react_to_post(user_id, post_id, same_reaction_type)

    # Assert
    deleted_reaction_return_false = Reaction.objects\
                                            .filter(
                                                reacted_by_id=user_id,
                                                post_id=post_id,
                                                reaction=reaction_type
                                            ).exists()

    assert deleted_reaction_return_false is  False


@pytest.mark.django_db
def test_react_to_post_when_invalid_user_id_raise_invalid_user_exception(
        data_pop
):

    # Arrange
    post_id = 2
    user_id = 0
    reaction_type = ReactionChoices.LOVE.value

    # Act
    with pytest.raises(InvalidUserException):
        react_to_post(user_id, post_id, reaction_type)


@pytest.mark.django_db
def test_react_to_post_when_invalid_post_id_raise_invalid_post_exception(
        data_pop
):

    # Arrange
    post_id = 0
    user_id = 2
    reaction_type = ReactionChoices.LOVE.value

    # Act
    with pytest.raises(InvalidPostException):
        react_to_post(user_id, post_id, reaction_type)


@pytest.mark.django_db
def test_react_to_post_when_invalid_reaction_type_raise_invalid_reaction_type(
        data_pop
):

    # Arrange
    post_id = 1
    user_id = 2
    reaction_type = 'NAMASTE'

    # Act
    with pytest.raises(InvalidReactionTypeException):
        react_to_post(user_id, post_id, reaction_type)
