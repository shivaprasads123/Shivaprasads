import requests
def delete():
    data = {
    "phone": "+91xxxxxxxxxx",
    "otp": 111111
}
    requests.delete('https://hbs-ob-stage.herokuapp.com/user')


