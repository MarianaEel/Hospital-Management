from xml.etree.ElementTree import tostring
import requests
import os
import json


class test_api():
    def __init__(self,mode) -> None:
        self.term_size = os.get_terminal_size()
        self.name = "name"
        self.url = 'http://34.238.84.218:8000/' if mode is 0 else 'http://127.0.0.1:8000/'
        self.infodir = "./test/testfile.json"
        with open(self.infodir) as json_file:
            self.info = json.load(json_file)
        

    def test(self):
        self.f = open("./test/testoutcome.txt", "a")
        purl = (self.url+self.name)

        print('=' * self.term_size.columns)
        print("Here goes "+self.name+" test")
        self.f.write('=' * self.term_size.columns+'\n')
        self.f.write("Here goes "+self.name+" test"+'\n')

        print('test get ')
        self.f.write('test get '+'\n')

        response = requests.get(purl)
        print(response.json())
        print(response)
        self.f.write(json.dumps(response.json(), indent=4)+'\n')
        self.f.write("<Response ["+str(response.status_code)+"]>"+'\n')

        assert(response.status_code == 200)

        print("test post ")
        self.f.write("test post "+'\n')
        postdata = self.info[self.name][0]["postdata"][0]

        response = requests.post(purl, postdata)
        print(response)
        self.f.write("<Response ["+str(response.status_code)+"]>"+'\n')

        assert(response.status_code == 200)

        response = requests.get(purl)
        print(response.json())
        self.f.write(json.dumps(response.json(), indent=4)+'\n')

        print("test put: ")
        self.f.write("test put: "+'\n')
        putdata = self.info[self.name][0]["putdata"][0]

        response = requests.put(purl, putdata)
        print(response)
        self.f.write("<Response ["+str(response.status_code)+"]>"+'\n')
        assert(response.status_code == 200)

        response = requests.get(purl)
        print(response.json())
        self.f.write(json.dumps(response.json(), indent=4)+'\n')

        print("test delete: ")
        self.f.write("test delete: "+'\n')
        delurl = purl + "?id="+self.info[self.name][0]["deletedata"][0]["id"]

        response = requests.request('DELETE', delurl)
        print(response)
        self.f.write("<Response ["+str(response.status_code)+"]>"+'\n')
        assert(response.status_code == 200)

        response = requests.get(purl)
        print(response.json())
        self.f.write(json.dumps(response.json(), indent=4)+'\n')

        self.f.close()

class test_patients(test_api):
    def __init__(self,mode) -> None:
        super().__init__(mode)
        self.name = "patients"

class test_staffs(test_api):
    def __init__(self,mode) -> None:
        super().__init__(mode)
        self.name = "staffs"

class test_datas(test_api):
    def __init__(self,mode) -> None:
        super().__init__(mode)
        self.name = "datas"

class test_chats(test_api):
    def __init__(self,mode) -> None:
        super().__init__(mode)
        self.name = "chats"


if __name__ == '__main__':
    f = open("./test/testoutcome.txt", "w")
    f.write("")
    f.close()
    test_p=test_patients(0)
    test_p.test()
    test_s=test_staffs(0)
    test_s.test()
    test_d=test_datas(0)
    test_d.test()
    test_c=test_chats(0)
    test_c.test()
