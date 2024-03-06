import os
import sys
import json

def clear_screen():
    if sys.platform == "linux":
        os.system("clear")
    else:
        os.system("cls")

def check_file():
    app_files = (os.path.isfile("ejercicio4/data/employees.json") and os.path.isfile("ejercicio4/data/payments.json") )
    if os.path.isdir("ejercicio4/data") and app_files:
        pass
    else:
        os.system("mkdir ejercicio4/data/")
        with open("ejercicio4/data/employees.json", "w") as file:
            json.dump({}, file, indent=4)
        with open("ejercicio4/data/payments.json", "w") as file:
            json.dump({}, file, indent=4)

def get_info(archivo:str):
    with open("ejercicio4/data/"+archivo, "r") as file:
        return json.load(file)

def json_update(data:dict, archivo:str):
    with open("ejercicio4/data/"+archivo, "w+") as file:
        json.dump(data, file, indent=4)