import requests
import json

base_url = "https://reqres.in/api"


def test_cerulean_is_color_1():
    url = base_url + '/unknown/1'
    response = requests.get(url)
    body = response.json()
    assert response.status_code == 200
    assert body["data"]["name"] == "cerulean"
