import requests
def test_get_request():
    response = requests.get("https://hbs-ob-stage.herokuapp.com/status")
    response_body=response.json()
    #assert response.headers["Content-Type"]== "application/json; charset=utf-8"
    assert response.status_code == 200

def test_post_request():
    create_user = {
    "name": "userApple12333",
    "phone": "+91xxxxxxxxx",
    "email": "userApple1@hashedin.com",
    "password": "admin888822222344343",
    "otp": 111111
}
    endpoint= "https://hbs-ob-stage.herokuapp.com/user"
    response=requests.post(url=endpoint, data=create_user)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 201 #getting 500 internal server error

def test_post_request():
    otp = {
    "phone": "+91xxxxxxxxxx"
}

    endpoint= "https://hbs-ob-stage.herokuapp.com/get_register_otp"
    response=requests.post(url=endpoint, data=otp)
    print(response.status_code)
    print(response.json())
    #assert response.status_code == 201

def delete():
    data = {
    "phone": "+91xxxxxxxxxx",
    "otp": 111111
}
    requests.delete('https://hbs-ob-stage.herokuapp.com/user')

