from module.user_management import patient
import requests

class test_api():        
    def __init__(self) -> None:
        pass
    def test_patient(self):
        purl = ('http://127.0.0.1:5000/patients')
        response = requests.get(purl)

        print('test get ')
        print (response.json())
        print (response)
        # assert(response == 0)

        print("test post ")
        adata = {
            "id" : "1",
            "name" : "Jason",
            "gender" : "male",
            "age" : "19",
        }
        response = requests.post(purl,adata)
        print (response)
        response = requests.get(purl)
        print (response.json())

        print ("test put: ")
        bdata = {
            "id" : "1",
            "name" : "Bason",
            "gender" : "male",
            "age" : "29",
        }
        response = requests.put(purl,bdata)
        print (response)
        response = requests.get(purl)
        print (response.json())

        print ("test delete: ")
        delurl = purl + "?id=1"
        response = requests.request('DELETE',delurl)
        print (response)
        response = requests.get(purl)
        print (response.json())

if __name__ == '__main__':
    testapi=test_api()
    testapi.test_patient()
