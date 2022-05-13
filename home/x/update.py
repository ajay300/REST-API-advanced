import json
import requests


def postapi():

    URL = "http://127.0.0.1:8000/app4/student/api/"

    
    data = {
        'id':1,
        
        'name':'Sunil',
        'phone': 30303030  , 
        'std':'X'
        
    }
    headers = {
        'content-Type':'application/json'
    }

    json_data = json.dumps(data)

    r = requests.put(URL ,headers=headers, data=json_data)
    data = r.json()
    print(data)

postapi()