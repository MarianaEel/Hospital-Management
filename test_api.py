from module.user_management import patient
import requests
import os

class test_api():        
    def __init__(self) -> None:
        self.term_size = os.get_terminal_size()
    def test_patient(self):
        print('=' * self.term_size.columns)
        print("Here goes patient test")
        purl = ('http://127.0.0.1:5000/patients')
        
        print('test get ')
        response = requests.get(purl)
        print (response.json())
        print (response.status_code)
        assert(response.status_code == 200)

        print("test post ")
        adata = {
            "id" : "1",
            "name" : "Jason",
            "gender" : "male",
            "age" : "19",
        }
        response = requests.post(purl,adata)
        print (response)
        assert(response.status_code == 200)
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
        assert(response.status_code == 200)
        response = requests.get(purl)
        print (response.json())

        print ("test delete: ")
        delurl = purl + "?id=1"
        response = requests.request('DELETE',delurl)
        print (response)
        assert(response.status_code == 200)
        response = requests.get(purl)
        print (response.json())

    def test_staff(self):
        print('=' * self.term_size.columns)
        print("Here goes staff test")
        purl = ('http://127.0.0.1:5000/staffs')
        
        print('test get ')
        response = requests.get(purl)
        print (response.json())
        print (response)
        assert(response.status_code == 200)

        print("test post ")
        adata = {
            "id" : "1",
            "name" : "Steven",
            "gender" : "male",
            "role" : "nurse",
            "title": "chief phisician",
            "departmentid":"1301",
            "departmentname":"Proctology"
        }
        response = requests.post(purl,adata)
        print (response)
        assert(response.status_code == 200)
        response = requests.get(purl)
        print (response.json())

        print ("test put: ")
        bdata = {
            "id" : "1",
            "name" : "Steve",
            "gender" : "male",
            "role" : "doctor",
            "title": "chief phisician",
            "departmentid":"1302",
            "departmentname":"Proctology"
        }
        response = requests.put(purl,bdata)
        print (response)
        assert(response.status_code == 200)
        response = requests.get(purl)
        print (response.json())

        print ("test delete: ")
        delurl = purl + "?id=1"
        response = requests.request('DELETE',delurl)
        print (response)
        assert(response.status_code == 200)
        response = requests.get(purl)
        print (response.json())
if __name__ == '__main__':
    testapi=test_api()
    testapi.test_patient()
    testapi.test_staff()
