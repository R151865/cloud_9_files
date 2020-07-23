import pytest
from freezegun import freeze_time
from fb_post.utils.get_post import get_post
from fb_post.exceptions import InvalidPostException
from fb_post.constants import ConstantDicts
pytestmark = pytest.mark.django_db


def function_to_compare_replies(dict1, dict2):

    function_to_compare_users(dict1['commenter'], dict2['commenter'])

    assert dict1["comment_id"] == dict2["comment_id"]
    assert dict1["commented_at"] == dict2["commented_at"]
    assert dict1["comment_content"] == dict2["comment_content"]

    assert dict1["reactions"]['count'] == dict2["reactions"]['count']
    assert dict1["reactions"]['type'].sort() == dict2["reactions"]['type'].sort()


def function_to_compare_comments(dict1, dict2):

    function_to_compare_users(dict1['commenter'], dict2['commenter'])

    assert dict1["comment_id"] == dict2["comment_id"]
    assert dict1["commented_at"] == dict2["commented_at"]
    assert dict1["comment_content"] == dict2["comment_content"]

    assert dict1["reactions"]['count'] == dict2["reactions"]['count']
    assert dict1["reactions"]['type'].sort() == dict2["reactions"]['type'].sort()
    assert dict1['replies_count'] == dict2['replies_count']


def function_to_compare_users(user1, user2):

    assert user1['user_id'] == user2['user_id']
    assert user1['name'] == user2['name']
    assert user1['profile_pic'] == user2['profile_pic']


def fucntion_to_compare_post_details(post1, post2):

    function_to_compare_users(post1['posted_by'], post2['posted_by'])

    assert post1['post_id'] == post2['post_id']
    assert post1['posted_at'] == post2['posted_at']
    assert post1['post_content'] == post2['post_content']
    assert post1['reactions']['count'] == post2['reactions']['count']
    assert post1['reactions']['type'].sort() == post2['reactions']['type'].sort()
    assert post1['comments_count'] == post2['comments_count']


def compare_comments_and_posts(post_comments, actual_post_comments):

    for j in range(len(post_comments)):
        for k in range(len(post_comments[j]['replies'])):

            function_to_compare_replies(
                post_comments[j]['replies'][k],
                actual_post_comments[j]['replies'][k])

        function_to_compare_comments(
            post_comments[j], actual_post_comments[j])


# this is function is used for user_posts and get_posts
def function_used_to_compare(post, actual_post):

    if post and actual_post:
        for i in range(len(post)):
            compare_comments_and_posts(
                post[i]['comments'], actual_post[i]['comments'])

            fucntion_to_compare_post_details(post[i], actual_post[i])

        return True
    else:
        return False


# Task - 13
# get_post
@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_get_post_with_valid_details_return_post_dict(factories_data_pop):

    # Arrange
    post_id = 1
    actual_post = [ConstantDicts.actual_post.value]

    # Act
    post = get_post(post_id)

    # Assert
    post = [post]
    output_is_true = function_used_to_compare(post, actual_post)

    print(post)
    assert  output_is_true is True

"""
@pytest.mark.django_db
@freeze_time("2012-01-14")
def test_get_post_when_invalid_post_id_given_raise_invalid_post_exception(data_pop):

    # Arrange
    post_id = 0

    # Act
    with pytest.raises(InvalidPostException):
        get_post(post_id)
"""