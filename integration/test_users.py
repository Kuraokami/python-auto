import requests
import json

base_url = "https://reqres.in/api"


def test_lindsay_ferguson_is_user_8():
    url = base_url + '/users/8'
    response = requests.get(url)
    body = response.json()
    assert response.status_code == 200
    assert body["data"]["email"] == "lindsay.ferguson@reqres.in"


def test_list_of_users_contains_6_elements():
    url = base_url + '/users'
    response = requests.get(url)
    body = response.json()
    assert len(body["data"]) == 6


def test_can_create_users():
    url = base_url + '/users'
    user_data = {"name": "Stephen Strange", "Job": "Supreme Sorcerer"}
    response = requests.post(url, json.dumps(user_data))
    body = response.json()
    assert response.status_code == 201
    assert "id" in body


def test_can_access_second_page():
    url = base_url + '/users?page=2'
    response = requests.get(url)
    body = response.json()
    assert response.status_code == 200
    assert 'data' in body
    assert len(body.get('data')) == 6


def test_user_data_is_complete():
    url = base_url + '/users/1'
    response = requests.get(url)
    body = response.json()
    assert response.status_code == 200
    assert len(body.get('data')) >= 5
    assert body.get('data')["email"] == "george.bluth@reqres.in"
    assert body.get('data')["id"] == 1
    assert body.get('data').get('first_name') == "George"
    assert body.get('data')["last_name"] == "Bluth"
    assert body.get('data')["avatar"] == "https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg"


def test_throws_404_when_erroneus_user():
    url = base_url + '/users/983'
    response = requests.get(url)

    assert response.status_code == 404


