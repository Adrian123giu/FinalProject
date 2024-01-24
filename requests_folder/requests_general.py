import requests

class GeneralRequests:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_invalid_endpoint():

        return requests.get(f"{GeneralRequests.BASE_URL}/invalidendpoint")

    @staticmethod
    def get_posts_for_response_time():

        return requests.get(f"{GeneralRequests.BASE_URL}/posts")