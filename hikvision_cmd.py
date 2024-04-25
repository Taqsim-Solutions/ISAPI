import requests
import json
from requests.auth import HTTPDigestAuth
from types import SimpleNamespace
import argparse

from AddFaceRecord import addFaceRecord
from DeleteFaceRecord import DeleteFaceRecord
from CreateUser import CreateUser
from DeleteUser import DeleteUser
from ListUser import ListUser
from ReadEvents import ReadEvents

def main():
    parser = argparse.ArgumentParser(description="Sistema de Lectura Relojes HIKVision")
    parser.add_argument("--order", help="Orden a Ejecutar")
    parser.add_argument("--host", help="Servidor Destino")
    parser.add_argument("--user", help="Usuario")
    parser.add_argument("--pass", help="Clave")
    args = parser.parse_args()
    
    return args.ifile, args.ofile, args.host, args.user, args.passwd
 
class hikvision():
    def __init__(self, user, password, url) -> None:
        self.__user = user
        self.__password = password
        self.__url = url

    def generar_auth (self, ):
        auth = HTTPDigestAuth(self.__user, self.__password)
        return auth

    def listUser (self):
        auth = self.generar_auth()
        ListUser(self.__url, auth, r'li_entrada.json')


url = 'http://192.168.68.200'
usuario = 'admin'
clave = 'ano2023-26455604'

hv = hikvision(usuario, clave, url)
hv.listUser()
