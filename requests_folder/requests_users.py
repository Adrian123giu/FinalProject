import requests

class UsersRequest:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_users():

        return requests.get(f"{UsersRequest.BASE_URL}/users")

    @staticmethod
    def get_user_by_id(user_id):

        return requests.get(f"{UsersRequest.BASE_URL}/users/{user_id}")