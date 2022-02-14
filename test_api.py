from module.user_management import patient
import requests


def test_user_management():
    response = requests.request("GET", 'http://127.0.0.1:5000/patients')
    print (response.json())
    print (response)
    # assert(response == 0)


if __name__ == '__main__':
    test_user_management()
