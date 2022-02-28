import requests

def test_get_request():
    response = requests.get("https://hbs-ob-stage.herokuapp.com/status")
    response_body=response.json()
    #assert response.headers["Content-Type"]== "application/json; charset=utf-8"
    assert response.status_code == 200
    #assert response_body['total'] == 12


