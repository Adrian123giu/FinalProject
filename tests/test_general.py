import pytest
from requests_folder.requests_general import GeneralRequests

class TestGeneral:

    def test_invalid_endpoint(self):

        response = GeneralRequests.get_invalid_endpoint()
        assert response.status_code == 404, "Status code pentru endpoint inexistent nu este 404"

    def test_response_time(self):

        response = GeneralRequests.get_posts_for_response_time()
        assert response.elapsed.total_seconds() < 2, "Timpul de răspuns este mai mare de 2 secunde"