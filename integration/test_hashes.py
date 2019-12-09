import requests
import json

base_url = "http://localhost:8088"


def test_hashes_are_returned():
    url = base_url + '/hash'
    user_data = {"password": "12345678"}
    
    response = requests.post(url, json.dumps(user_data))

    id = response.text

    get_url = base_url + '/hash/' + id

    hash_response = requests.get(get_url)
    assert hash_response.status_code == 200
    

def test_input_must_be_enforced():
    url = base_url + '/hash'
    user_data = {"foo": "bar", "test" : "bruh!!!"}
    
    response = requests.post(url, json.dumps(user_data))

    assert response.status_code == 404, "Application should return error when input is misformated"

def test_hashes_should_be_salted():
    url = base_url + '/hash'
    user_data = {"password": "12345678"}
    
    first_response = requests.post(url, json.dumps(user_data))
    second_response = requests.post(url, json.dumps(user_data))

    first_id = first_response.text
    second_id = second_response.text

    first_hash_url = base_url + '/hash/' + first_id
    second_hash_url = base_url + '/hash/' + second_id

    first_hash_response = requests.get(first_hash_url)
    second_hash_response = requests.get(second_hash_url)
    assert first_hash_response.status_code == 200
    assert second_hash_response.status_code == 200
    assert second_hash_response.text != first_hash_response.text, "Equal Passwords should be hashed differently by using salt."


def test_url_must_errors_must_be_managed_gracefully():
    url = base_url + '/hash/foo'
    
    response = requests.get(url)

    assert response.status_code == 400, "Application should return error when input is misformated"
    assert "strconv.Atoi:" not in response.text, "Too much information displayed, Possible attack vector"
    