import requests
import json

url = "http://127.0.0.1:8000/app3/api/"





def get_data(id=None):
    data = {}
    headers = {
        'content-Type':'application/json'
    }

    if id is not None:
        data = {'id',id}
    json_data = json.dumps(data)
    r = requests.get(url ,headers=headers, data=json_data)
    data = r.json()
    print(data)

get_data()

        
