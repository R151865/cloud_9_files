from django.utils import timezone
import pytest
from freezegun import freeze_time
from fb_post.models import Reaction
from fb_post.constants import ReactionChoices
from fb_post.exceptions import (
    InvalidReactionTypeException,
    InvalidCommentException,
    InvalidUserException
    )
from fb_post.utils.react_to_comment import react_to_comment
pytestmark = pytest.mark.django_db


# Task - 6
#react to comment

@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_react_to_comment_with_valild_details_react_to_comment(data_pop):

    # Arrange
    comment_id = 1
    user_id = 2
    reaction_type = ReactionChoices.LIT.value

    # Act
    react_to_comment(user_id, comment_id, reaction_type)

    # Assert
    reaction = Reaction.objects.all().last()

    assert reaction.reaction == reaction_type
    assert reaction.comment_id == comment_id
    assert reaction.reacted_by_id == user_id
    assert reaction.reacted_at == timezone.now()


@pytest.mark.django_db
@freeze_time("2012-01-14")
@pytest.mark.parametrize('reaction_type, updated_reaction_type', [
    (ReactionChoices.LIT.value, ReactionChoices.THUMBS_DOWN.value),
    (ReactionChoices.THUMBS_DOWN.value, ReactionChoices.LIT.value),
    (ReactionChoices.ANGRY.value, ReactionChoices.SAD.value)
    ])
def test_react_to_comment_when_diffent_reactions_given_by_same_user_update_reaction(
        data_pop,
        updated_reaction_type,
        reaction_type
):

    # Arrange
    comment_id = 1
    user_id = 6
    react_to_comment(user_id, comment_id, reaction_type)

    # Act
    react_to_comment(user_id, comment_id, updated_reaction_type)

    # Assert
    reaction = Reaction.objects.all().last()

    assert reaction.reaction == updated_reaction_type
    assert reaction.comment_id == comment_id
    assert reaction.reacted_by_id == user_id
    assert reaction.reacted_at == timezone.now()


@pytest.mark.django_db
def test_react_to_comment_delete_reaction_type_when_same_reaction_type_given_by_same_user(
        data_pop
):

    # Arrange
    comment_id = 1
    user_id = 6
    reaction_type = ReactionChoices.LOVE.value
    same_reaction_type = ReactionChoices.LOVE.value
    react_to_comment(user_id, comment_id, reaction_type)

    # Act
    react_to_comment(user_id, comment_id, same_reaction_type)

    # Assert
    is_same_reaction_deleted = Reaction.objects\
                                       .filter(
                                           reacted_by_id=user_id,
                                           comment_id=comment_id,
                                           reaction=reaction_type
                                       ).exists()

    assert is_same_reaction_deleted is False


@pytest.mark.django_db
def test_react_to_comment_when_invalid_user_id_raise_invalid_user_exception(
        data_pop
):

    # Arrange
    comment_id = 1
    user_id = 0
    reaction_type = ReactionChoices.LOVE.value

    # Act
    with pytest.raises(InvalidUserException):
        react_to_comment(user_id, comment_id, reaction_type)


@pytest.mark.django_db
def test_react_to_comment_when_invalid_post_id_raise_invalid_user_exception(
        data_pop
):

    # Arrange
    comment_id = 0
    user_id = 1
    reaction_type = ReactionChoices.LOVE.value

    # Act
    with pytest.raises(InvalidCommentException):
        react_to_comment(user_id, comment_id, reaction_type)


@pytest.mark.django_db
def test_react_to_comment_when_invalid_reaction_type_raise_invalid_reaction_type(
        data_pop
):

    # Arrange
    comment_id = 1
    user_id = 3
    reaction_type = 'NAMASTE reaction'

    # Act
    with pytest.raises(InvalidReactionTypeException):
        react_to_comment(user_id, comment_id, reaction_type)
