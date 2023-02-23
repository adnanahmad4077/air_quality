from ssapythontools import database as db
import requests
import json
import time


def getAllSensors(key):
    url = "http://api.breathelondon.org/api/ListSensors?key="+key
    response = requests.request("GET", url)
    result = json.loads(response.text)
    return result[0]

def insertSensors(data):
    with db.create_connection_mssql('SSAVMTSQL02,60531', 'PentanaSSAPI') as conn:
        conn.execute(query)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    key = "a6f0958e-b753-11ec-b909-0242ac120002"
    sensors = getAllSensors(key)
