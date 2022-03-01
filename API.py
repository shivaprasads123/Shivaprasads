import requests


def test_get_request():
    response = requests.get("https://hbs-ob-stage.herokuapp.com/status")
    response_body = response.json()
    assert response.headers["Content-Type"] == "application/json"
    print(response.status_code)
    assert response.status_code == 200


def test_post_request():
    payload = { "name": "jainsus",
    "phone": "+91xxxxxxxxx",
    "email": "tuser@hashe.com",
    "password": "admin@1237",
    "otp": 111111
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/user"
    response = requests.post(endpoint, json=payload)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 400


def test_post_get_otp():
    payload = {
        "phone": "+91xxxxxxxxxx"
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/get_register_otp"
    response = requests.post(url=endpoint, json=payload)
    print(response.json())
    assert response.status_code == 200


def test_delete():
    payload = {
        "phone": "+91xxxxxxxxxx"
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/user"
    response = requests.post(url=endpoint, json=payload)
    print(response.json())
    assert response.status_code == 400


def test_edit():
    payload = {
    "name": "user",
    "phone": "+91xxxxxxxxx",
    "email": "userq@hashedin.com",
    "password": "admin",
    "otp": 111111
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/user"
    response = requests.put(endpoint, json=payload)
    assert response.status_code == 400


def test_login_otp():
    payload = {
    "phone": "+91xxxxxxxx"
}
    endpoint = "https://hbs-ob-stage.herokuapp.com/get_otp"
    response = requests.post(endpoint, json=payload)
    assert response.status_code==200


def test_authenticate_pass():
    payload = {

            "phone": "+91xxxxxxxx",
            "LoginType": "admin@12378",
            "password": "admin@123"
        }
    endpoint = "https://hbs-ob-stage.herokuapp.com/authenticate"
    response = requests.post(endpoint, json=payload)
    assert response.status_code==200


def test_authenticate_otp():
    payload = {

    "phone": "+91xxxxxxxx",
    "LoginType": "OTP",
    "otp": 111111
        }
    endpoint = "https://hbs-ob-stage.herokuapp.com/authenticate"
    response = requests.post(endpoint, json=payload)
    assert response.status_code==201


def test_login():
    headers =  {"Authorization": "Bearer Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjQ2MDM3MTIyLCJqdGkiOiI5YjY1YTE3MS0xN2U5LTQ4ZGItOTEyMy1mYjgwYzI5NjI1MWUiLCJuYmYiOjE2NDYwMzcxMjIsInR5cGUiOiJhY2Nlc3MiLCJzdWIiOiI2MjE4Yjk0NjllYWY2ZDY4OTg0MWIzYWQiLCJleHAiOjE2NDYwMzgwMjJ9.SAWM23-nUvYWcOzwcPRUZxIyOx_GuoiqdEDpekAm2j4"}
    endpoint = "https://hbs-ob-stage.herokuapp.com/protected_test"
    response = requests.get(endpoint, Type = headers)
    assert  response.status_code == 200


