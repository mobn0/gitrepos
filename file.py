from os import listdir
from time import sleep
from ast import literal_eval

def check_file():
    if "NFC_MAP.json" not in listdir():
        with open("NFC_MAP.json", "w") as map:
            map.write("{}")

def get_map():
    with open("NFC_MAP.json") as map:
        return literal_eval(map.read())

def update_map(updated_map):
    with open("NFC_MAP.json", "w") as map:
        map.write(str(updated_map))

while True:

    check_file()

    map = get_map()
    map["19"] = 1
    update_map(map)

    sleep(5)