import requests

BASE_URL = "https://petstore.swagger.io/v2"


def test_add_new_pet():
    pet_data_for_adding = {"name": "test_name", "photoUrls": ["https://testurls/test"]}

    response = requests.post(f"{BASE_URL}/pet", json=pet_data_for_adding)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["name"] == pet_data_for_adding["name"]
