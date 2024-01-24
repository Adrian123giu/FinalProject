import pytest
from requests_folder.requests_comments import CommentsRequest

class TestComments:

    def test_get_comments(self):
        response = CommentsRequest.get_comments()
        assert response.status_code == 200
        assert len(response.json()) > 0, "Nu au fost returnate comentarii"

    def test_get_comments_by_post_id(self):
        post_id = 1
        response = CommentsRequest.get_comments_by_post_id(post_id)
        assert response.status_code == 200
        for comment in response.json():
            assert comment['postId'] == post_id, "ID-ul postului pentru comentarii nu corespunde"