import json

def load_participants(path):
    with open(path, "r") as file:
        data = json.load(file)
    return data
