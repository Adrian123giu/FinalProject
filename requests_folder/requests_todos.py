import requests

class TodosRequest:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_todos():

        return requests.get(f"{TodosRequest.BASE_URL}/todos")

    @staticmethod
    def get_todo_by_id(todo_id):

        return requests.get(f"{TodosRequest.BASE_URL}/todos/{todo_id}")