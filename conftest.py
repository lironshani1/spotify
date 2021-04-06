import pytest
from definitions import TEST_FILE
import json
from Infra.REST import *
from urllib.parse import urljoin


@pytest.fixture(scope="function", autouse=True)
def get_url():
    yield "http://localhost:9090"


@pytest.fixture(scope="function", autouse=True)
def get_tests_data():
    with open(file=TEST_FILE, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    yield data


@pytest.fixture(scope="function", autouse=True)
def delete_all_data(get_url):
    improved_delete(url=urljoin(get_url, "/admin/delete_all_users"))

