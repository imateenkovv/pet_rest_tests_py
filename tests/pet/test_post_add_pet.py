import requests

BASE_URL = "https://petstore.swagger.io/v2"
GOAL_URL = f"{BASE_URL}/pet"

def test_add_new_pet():
    pet_data_for_adding = {"name": "test_name", "photoUrls": ["https://testurls/test"]}

    response = requests.post(GOAL_URL, json=pet_data_for_adding)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["name"] == pet_data_for_adding["name"]

def test_add_new_pet_with_empty_body():
    pet_data_for_adding = {}
    response = requests.post(GOAL_URL, json=pet_data_for_adding)
    assert response.status_code == 400