import requests
import json
from types import SimpleNamespace

from requests.auth import HTTPDigestAuth

usuario = 'admin'
clave = '1234567X'

auth=HTTPDigestAuth(usuario, clave)

path = 'http://192.168.0.64/ISAPI/AccessControl/UserInfo/Record?format=json'

json_data = [] # your list with json objects (dicts)

with open('mass_addUser.json') as json_file:
   json_data = json.load(json_file)

for item in json_data:
    for body in item['UserInfo']:
        response = requests.post(path, data=json.dumps(body), auth=auth)
        result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
        print(result)