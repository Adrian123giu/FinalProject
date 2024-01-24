import requests

class PostsRequest:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_posts():
       
        return requests.get(f"{PostsRequest.BASE_URL}/posts")

    @staticmethod
    def create_post(data):
       
        return requests.post(f"{PostsRequest.BASE_URL}/posts", json=data)

    @staticmethod
    def get_post_by_id(post_id):

        return requests.get(f"{PostsRequest.BASE_URL}/posts/{post_id}")
