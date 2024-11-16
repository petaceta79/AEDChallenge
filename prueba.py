from rich import print
from participant import load_participants



# Funciones 
# Sumar amigos 
def Amigos(participanteI, participanteE, puntos):
    total = 0
    if (participanteI.id in participanteE.friend_registration):
        total = puntos
    return total
# Sumar idiomas 
def Idiomas(participanteI, participanteE, puntos):

# Sumar Experiencia 
def Experiencia(participanteI, participanteE, puntos):
    


# Ruta al archivo JSON
data_path = "data/datathon_participants.json"
# Cargar participantes
participants = load_participants(data_path)



# Inicialización de la lista de grupos
revision = [] # Lista que contendrá sublistas [name, puntos], al final de cada itineracion se reinicia, sirve para comparar al final 
grupos = []  # Lista que contendrá los grupos, cada grupo será otra lista de participantes



# Algoritmo para formar grupos
for i, participant_i in enumerate(participants, start=1):
    if (participant_i not in grupos): 
        for e, participant_e in enumerate(participants, start=1):
            # Evitar que un participante sea comparado consigo mismo
            if i != e and participant_e not in grupos: 
                revision.append([participant_e.id,0])
                revision[-1][1] += Amigos(participant_i,participant_e,100)


                   

     
            

# Mostrar los grupos creados
for grupo in grupos:
    print(f"Grupo: {[p.name for p in grupo]}")






