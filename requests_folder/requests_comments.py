import requests

class CommentsRequest:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_comments():

        return requests.get(f"{CommentsRequest.BASE_URL}/comments")

    @staticmethod
    def get_comments_by_post_id(post_id):

        return requests.get(f"{CommentsRequest.BASE_URL}/comments", params={"postId": post_id})