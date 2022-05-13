import requests
import json


def postapi():

    URL = "http://127.0.0.1:8000/employee/api/"
    url2 = "http://127.0.0.1:8000/app4/student/api/"

    
    '''
        n = input("Enter a  name : ")
        p = int(input('Enter a phone : '))
        ep = int(input("Enter your Id : "))
        e = input("Enter a email : ")
        l = input("location : ")

        data = {
            'name':n,
            'phone': p , 
            'emp_id': ep , 
            'email' : e,
            'location' : l,
        }
    '''
    data = {
        'seat_no':1,
        'name':'Hitesh',
        'phone':70707070,
        'std' : 'X'

    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url2 ,headers=headers, data=json_data)
    data = r.json()
    print(data)

postapi()




