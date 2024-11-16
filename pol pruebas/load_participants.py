import json
import os

def load_participants(filename):
    # Construir ruta absoluta al archivo
    absolute_path = os.path.join(os.path.dirname(__file__), filename)

    # Cargar el archivo JSON
    with open(absolute_path, "r") as file:
        return json.load(file)
