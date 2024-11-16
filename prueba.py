from rich import print
from participant import load_participants



# Funciones 
def calculate_score(p1):
    score = 0

    if (p1.experience_level == "Intermediate"):
        score += 10
    

    return score



# Ruta al archivo JSON
data_path = "data/datathon_participants.json"
# Cargar participantes
participants = load_participants(data_path)



# Inicialización de la lista de grupos
Puntuacion = []
grupos = []  # Lista que contendrá los grupos, cada grupo será otra lista de participantes



# Algoritmo para formar grupos
for i, participant_i in enumerate(participants, start=1):
    Puntuacion.append([participant_i.id, calculate_score(participant_i)])

Puntuacion.sort(key=lambda x: x[1])



for i, Puntuacio in enumerate(Puntuacion, start=1):
    print(Puntuacio)
      


print("-------------------------")




# Mostrar los grupos creados
for i, grupo in enumerate(grupos, start=1):
    # Imprimimos el número de grupo y los integrantes
    print(f"{i}: {', '.join(grupo)}")




