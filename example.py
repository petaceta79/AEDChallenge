from rich import print
from participant import load_participants

# Ruta al archivo JSON
data_path = "data/datathon_participants.json"

# Cargar participantes
participants = load_participants(data_path)

# Acceder al nombre del primer participante
print(participants[0].name)
