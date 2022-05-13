import requests 

def getapibyid():
    while True:
        id = int(input("Enter a number :"))
        URl = f"http://127.0.0.1:8000/employee/{id}/"

        r = requests.get(url=URl)

        data = r.json()
        print(data)
getapibyid()

