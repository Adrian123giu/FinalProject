import pytest
from requests_folder.requests_posts import PostsRequest

class TestPosts:

    def test_get_posts(self):
        response = PostsRequest.get_posts()
        assert response.status_code == 200
        assert len(response.json()) == 100, "Numărul de postări returnat nu este 100"

    def test_create_post(self):
        data = {"title": "New Post", "body": "This is a new post", "userId": 1}
        create_response = PostsRequest.create_post(data)
        assert create_response.status_code == 201
        assert create_response.json()['title'] == data['title']

        get_response = PostsRequest.get_posts()
        assert get_response.status_code == 200
        assert any(post['title'] == data['title'] for post in get_response.json())

    def test_get_post_by_id(self):
        post_id = 1
        response = PostsRequest.get_post_by_id(post_id)
        assert response.status_code == 200
        assert response.json()['id'] == post_id, "ID-ul postului nu corespunde"