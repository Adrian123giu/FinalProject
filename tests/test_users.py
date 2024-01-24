import pytest
from requests_folder.requests_users import UsersRequest

class TestUsers:

    def test_get_users(self):
        response = UsersRequest.get_users()
        assert response.status_code == 200
        assert len(response.json()) > 0, "Nu au fost returnați utilizatori"

    def test_get_user_by_id(self):
        user_id = 1
        response = UsersRequest.get_user_by_id(user_id)
        assert response.status_code == 200
        assert response.json()['id'] == user_id, "ID-ul utilizatorului nu corespunde"