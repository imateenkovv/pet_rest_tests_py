import pytest
import requests
import json
import logging

# Срхраняем оригинальный метод чтобы не потерять
original_send = requests.Session.send


def logging_send(self, *args, **kwargs):
    """Наш метод который перехватывает вызов и логирует и отдает результат"""
    response = original_send(self, *args, **kwargs)

    logging.info(f"--- Request Sent ---")
    logging.info(f"URL: {response.request.url}")
    logging.info(f"Method: {response.request.method}")
    logging.info(f"--- Response Received ---")
    logging.info(f"Status Code: {response.status_code}")
    try:
        response_json = response.json()
        pretty_json = json.dumps(response_json, indent=4, ensure_ascii=False)
        logging.info(f"Response Body (JSON):\n{pretty_json}")
    except json.JSONDevodeError:
        logging.info(f"Response Body (Raw):\n{response.text}")
        return response


@pytest.fixture(scope="session", autouse=True)
def patch_requests_send():
    # Настраиваем базовый логгер
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    requests.Session.send = logging_send

