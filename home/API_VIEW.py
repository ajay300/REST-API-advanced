
import requests
import json


#for view data by id 
def getapibyid():
    while True:
        id = int(input("Enter your id :"))
        URl = f"http://127.0.0.1:8000/employee/{id}/"

        r = requests.get(url=URl)

        data = r.json()
        print(data)
        exite = input("Do you want to view more or 'exit' : ")
        if exite == "exit":
            alldata()


#For view all data
def alldata():
    URl = "http://127.0.0.1:8000/employee/"

    r = requests.get(url=URl)

    l = r.json()
    print(l)


#For POST a DATA
def postapi():
    URL = "http://127.0.0.1:8000/employee/"

    while True: 
        n = input("Enter a  name : ")
        p = int(input('Enter a phone : '))
        e = input("Enter a email : ")
        l = input("location : ")

        data = {
            'name':n,
            'phone': p , 
            'email' : e,
            'location' : l,
        }

        json_data = json.dumps(data)

        r = requests.post(URL , data=json_data)
        print("****Your Data has been Added.!****")
        exite = input("Do you want to add more data or want to exit : ")
        if exite == "exit":
            alldata()
        else : 
            postapi()


def viewapi():
    op = int(input("Enter Method (GET = 1 , POST = 2) : "))

    if op == 1:
        view = int(input("(By Id = 1) or (All data = 2) : "))
        if view == 1:
            getapibyid()
        else :
            alldata()
    elif op == 2 : 
        postapi()
    else : 
        print("Invalid input.")
        viewapi()

print("Enter only in Numbers...")
viewapi()