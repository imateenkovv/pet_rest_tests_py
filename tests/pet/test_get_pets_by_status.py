
import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"
GOAL_URL = f"{BASE_URL}/pet/findByStatus"

# Используем параметризацию для статусов
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_get_pets_by_status(status):

    response = requests.get(
        GOAL_URL, params={"status": status}
    )
    assert response.status_code == 200, f"Status code is not 200 for status '{status}'"
    response_json = response.json()
    assert isinstance(response_json, list), "Response is not a list"
    for pet in response_json:
        assert pet['status'] == status, f"Pet with id {pet.get('id')} has wrong status"