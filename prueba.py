from rich import print
from participant import load_participants

# Ruta al archivo JSON
data_path = "data/datathon_participants.json"

# Cargar participantes
participants = load_participants(data_path)

# Recorrer la lista de participantes y mostrar sus nombres
for i, participant in enumerate(participants, start=1):
    print(f"Participante {i}: {participant.name}")
