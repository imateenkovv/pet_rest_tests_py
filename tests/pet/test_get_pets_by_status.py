import requests

BASE_URL = "https://petstore.swagger.io/v2"


def test_get_pets_by_status_avialable():
    response = requests.get(
        f"{BASE_URL}/pet/findByStatus", params={"status": "available"}
    )
    assert response.status_code == 200


def test_get_pets_by_status_sold():
    response = requests.get(
        f"{BASE_URL}/pet/findByStatus", params={"status":"sold"}
    )
    assert response.status_code == 200


def test_get_pets_by_status_pending():
    response = requests.get(
        f"{BASE_URL}/pet/findByStatus", params={"status":"pending"}
    )
    assert response.status_code == 200