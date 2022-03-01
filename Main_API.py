import requests
import json
import jsonpath

def Test_Rigester_User_post():
    payload={
        "name": "Muhammad Nur Ali",
        "email": "muh.nurali43@gmail.com",
        "password": "12345678",
        "age": 20
        }
    endpoint = "https://api-nodejs-todolist.herokuapp.com/user/register"
    response = requests.post(endpoint, json=payload)
    assert response.headers["Content-Type"] == "application/json"
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200

def test_post_login():
    payload = {
	"email": "muh.nurali43@gmail.com",
	"password": "12345678"
}
    endpoint = "https://api-nodejs-todolist.herokuapp.com/user/login"
    response = requests.post(endpoint, json=payload)
    assert response.headers["Content-Type"] == "application/json"; charset=utf-8
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200

def test_post_logout():
    headers = {
        "Authorization": "Bearer Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZGRiZGQxM2JiMjIzZTEyMjY5NzMxMmEiLCJpYXQiOjE1NzQ2OTEwNDl9.R4sJr3wnoiG_HwKT3to40u6Z1b_CiClH66sJZRRj9bA"}
    endpoint = "https://api-nodejs-todolist.herokuapp.com/user/logout"
    response = requests.get(endpoint, Type=headers)
    assert response.status_code == 200

def test_get_loggedin_token():
    response = requests.get("https://api-nodejs-todolist.herokuapp.com/user/me")
    headers = {
        "Authorization": "Bearer Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZGRjY2JlYzZiNTVkYTAwMTc1OTcyMmMiLCJpYXQiOjE1NzQ3NTE2ODh9.GPbsl9FLX4VrsGVErodiXypjuz1us4tfD0jwg2_UrzY " }
    print(response.status_code)
    assert response.status_code == 200

def update_user_put():
    response = requests.put('endpoint', data={'key': 'value'})
    endpoint = "https://api-nodejs-todolist.herokuapp.com/user/me"
    data = {"Authorization" : "Bearer Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZGRjY2JlYzZiNTVkYTAwMTc1OTcyMmMiLCJpYXQiOjE1NzQ3NTE2ODh9.GPbsl9FLX4VrsGVErodiXypjuz1us4tfD0jwg2_UrzY"}

def post_upload_image():
    headers = {
        "Authorization": "Bearer Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZGRiZGQxM2JiMjIzZTEyMjY5NzMxMmEiLCJpYXQiOjE1NzQ2OTEwNDl9.R4sJr3wnoiG_HwKT3to40u6Z1b_CiClH66sJZRRj9bA"}
    endpoint = "https://api-nodejs-todolist.herokuapp.com/user/me/avatar"
    response = requests.get(endpoint, Type=headers)
    assert response.status_code == 200

def get_image():
    response = requests.get("https://api-nodejs-todolist.herokuapp.com/user/5ddccbec6b55da001759722c/avatar")
    print(response.status_code)

def delete_image():
    response = requests.delete('https://api-nodejs-todolist.herokuapp.com/user/me/avatar')
    headers = {
        "Authorization": "Bearer Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZGRiZGQxM2JiMjIzZTEyMjY5NzMxMmEiLCJpYXQiOjE1NzQ2OTY1NzF9.5v32aulIG6tk91_oOehOexSqDst-YgYHGwD803ZSP_I" }
    print(response.status_code)

def delete_user():
    response = requests.delete('https://api-nodejs-todolist.herokuapp.com/user/me')
    headers = {
        "Authorization": "Bearer Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZGRiZGQxM2JiMjIzZTEyMjY5NzMxMmEiLCJpYXQiOjE1NzQ2OTY1NzF9.5v32aulIG6tk91_oOehOexSqDst-YgYHGwD803ZSP_I" }
    print(response.status_code)
