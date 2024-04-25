import requests
import json

def CreateUser(url, auth, ifile):
    path = f'{url}/ISAPI/AccessControl/UserInfo/Record?format=json'

    with open(ifile, 'r') as archivo:
        json_data = json.load(archivo)
    
    response = requests.post(path, auth=auth, json=json_data)

    if response.status_code == 200:
        json_data = response.json()
        print(json_data)
        print(response.text)
    else:
        print('Error:', response.status_code)
