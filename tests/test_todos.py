import pytest
from requests_folder.requests_todos import TodosRequest

class TestTodos:

    def test_get_todos(self):
        response = TodosRequest.get_todos()
        assert response.status_code == 200
        assert len(response.json()) > 0, "Nu au fost returnate todo-uri"

    def test_get_todo_by_id(self):
        todo_id = 1
        response = TodosRequest.get_todo_by_id(todo_id)
        assert response.status_code == 200
        assert response.json()['id'] == todo_id, "ID-ul todo nu corespunde"