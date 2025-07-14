import requests

BASE_URL = "https://petstore.swagger.io/v2"


def test_get_pets_by_status_avialable():
    response = requests.get(
        f"{BASE_URL}/pet/findByStatus", params={"status": "available"}
    )
    assert response.status_code == 200
