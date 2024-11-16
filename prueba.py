from rich import print
from participant import load_participants



# Funciones 
# Sumar 
def Amigos(participanteI, participanteE, puntos):
    total = 0
    if (participanteI.id in participanteE.friend_registration):
        total = puntos
    return total



# Ruta al archivo JSON
data_path = "data/datathon_participants.json"
# Cargar participantes
participants = load_participants(data_path)



# Recorrer la lista de participantes y mostrar sus nombres
#for i, participant in enumerate(participants, start=1):
#    print(f"Participante {i}: {participant.friend_registration}")



# Inicialización de la lista de grupos
revision = [] # Lista que contendrá sublistas [name, puntos], al final de cada itineracion se reinicia, sirve para comparar al final 
grupos = []  # Lista que contendrá los grupos, cada grupo será otra lista de participantes



# Algoritmo para formar grupos
for i, participant_i in enumerate(participants, start=1):
    for e, participant_e in enumerate(participants, start=1):
        # Evitar que un participante sea comparado consigo mismo
        if i != e: 
            revision.append([participant_e.name,0])
            revision[-1][1] += Amigos(participant_i,participant_e,100)
        
     
            

# Mostrar los grupos creados
for grupo in grupos:
    print(f"Grupo: {[p.name for p in grupo]}")






