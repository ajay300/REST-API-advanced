import requests
import json

url = "http://127.0.0.1:8000/app4/student/api/1"


def delete_data():

    data = {
        'id' : 1
    }
    headers = {
        'content-Type':'application/json'
    }

    json_data = json.dumps(data)
    r = requests.delete(url=url,headers=headers , data=json_data)
    data = r.json()
    print(data)

delete_data()