import requests
response = requests.request("GET", 'http://127.0.0.1:5000/patients')
print (response.json())