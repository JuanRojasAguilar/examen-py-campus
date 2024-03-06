import os
import sys
import json

def clear_screen():
    if sys.platform == "linux":
        os.system("clear")
    else:
        os.system("cls")

def check_file():
    if os.path.isdir("ejercicio3/data") and os.path.isfile("ejercicio3/data/products.json"):
        pass
    else:
        os.system("mkdir ejercicio3/data/")
        with open("ejercicio3/data/products.json", "w") as file:
            json.dump({}, file, indent=4)

def get_info():
    with open("ejercicio3/data/products.json", "r") as file:
        return json.load(file)

def json_update(data:dict):
    with open("ejercicio3/data/products.json", "w+") as file:
        json.dump(data, file, indent=4)