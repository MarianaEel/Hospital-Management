from module.user_management import patient
import requests


def test_user_management():
    purl = ('http://127.0.0.1:5000/patients')
    response = requests.get(purl)
    print (response.json())
    print (response)
    # assert(response == 0)
    adata = {
        "id" : 1,
        "name" : "Jason",
        "gender" : "male",
        "age" : 19,
    }
    response = requests.post(purl,adata)
    print (response)
    response = requests.get(purl)
    print (response.json())

if __name__ == '__main__':
    test_user_management()
