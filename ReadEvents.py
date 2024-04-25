import requests
from datetime import datetime
from datetime import datetime
import pytz

def ReadEvents(url, auth, fdesde, fhasta):
    def convert_to_utc(time_str):
        time = datetime.strptime(time_str, '%Y-%m-%d')
        time_utc = time.astimezone(pytz.utc)
        time_utc_str = time_utc.strftime('%Y-%m-%dT00:00:00-07:00')
        return time_utc_str

    def json_entrada_leer(fdesde, fhasta, pos=0):
        startTime = str(convert_to_utc(fdesde))
        endTime = str(convert_to_utc(fhasta))
        json_data = {
            "AcsEventCond": {
                "searchID": "0",
                "searchResultPosition": pos,
                "maxResults": 30,
                "major": 5,
                "minor": 75,
                "startTime": startTime,  # "2024-03-01T01:00:00-07:00",
                "endTime": endTime  # "2024-04-03T23:59:59-07:00"
            }
        }
        return json_data

    path = f'{url}/ISAPI/AccessControl/AcsEvent?format=json'
    pos = 0
    total_registros = None
    while True:
        json_entrada = json_entrada_leer(fdesde, fhasta, pos)
        response = requests.post(path, auth=auth, json=json_entrada)
        if response.status_code == 200:
            json_data = response.json()
            if total_registros == None:
                total_registros = json_data["AcsEvent"]["totalMatches"]
            if int(json_data["AcsEvent"]["numOfMatches"]) > 0:
                try:
                    for info in json_data["AcsEvent"]["InfoList"]:
                        fecha, hora = info['time'].split('T')
                        hora_minutos = hora.split(':')[0:2]
                        hora_minutos_str = ":".join(hora_minutos)
                        print(
                            f"Fecha={fecha}\tHora={hora_minutos_str}\tNombre={info['name']}\tId={info['employeeNoString']}\tTipo={info['currentVerifyMode']}")
                    pos = pos + 30
                except:
                    print(json_data)
                    break
            else:
                break
        else:
            # Si la solicitud no fue exitosa, imprimir el código de estado
            print('Error:', response.status_code)
            break
    print(f'Cantidad de Registros Visualizado: {total_registros}')
