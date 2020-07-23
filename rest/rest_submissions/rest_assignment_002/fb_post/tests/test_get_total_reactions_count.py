import pytest
from freezegun import freeze_time
from fb_post.utils.get_total_reaction_count import get_total_reaction_count
pytestmark = pytest.mark.django_db


# Task - 7
# total reaction_count
@pytest.mark.django_db
def test_total_reaction_count_with_valid_details_return_count(
        data_pop
):

    # Arrage
    expected_dict = {'count': 18}

    # Act
    actual_dict = get_total_reaction_count()

    # Assert
    assert actual_dict == expected_dict

@pytest.mark.django_db
def test_total_reaction_count_when_no_reactions_in_database_return_count_zero():

    # Arrage
    expected_dict = {'count': 0}

    # Act
    actual_dict = get_total_reaction_count()

    # Assert
    assert actual_dict == expected_dict
