import requests
import json
from types import SimpleNamespace

from requests.auth import HTTPDigestAuth

usuario = 'admin'
clave = '1234567X'

auth=HTTPDigestAuth(usuario, clave)
url = 'http://192.168.0.64/ISAPI/Intelligent/FDLib/FDSetUp?format=json'
body = {
    "faceLibType": "blackFD",
    "FDID": '3',
    "FPID": '2',
    "faceURL": 'https://img001.prntscr.com/file/img001/4ZIKaJ4sSm6dBGSC3AnHtA.png'
    }
response = requests.put(url, data=json.dumps(body), auth=auth)


result = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
print(result)