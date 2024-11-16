from rich import print
from participant import load_participants



# Funciones 

# Objetivos 
# Función para detectar el grupo de palabras clave en una descripción
def asignar_cluster(descripcion):
    # Diccionario con las palabras clave para cada grupo
    palabras_clave = {
        "WIN": ["top", "win", "first", "trophy", "winning", "competitive"],
        "FRIENDS": ["friends", "meet", "new", "people", "connections", "social"],
        "LEARN": ["learn", "try", "abilities", "skills", "growth", "learning", "code"]
    }
    descripcion = descripcion.lower().strip()  # Convertir a minúsculas y eliminar espacios extra
    scores = {categoria: 0 for categoria in palabras_clave}  # Inicializar el puntaje para cada categoría

    # Para cada categoría, contar cuántas veces aparece alguna de las palabras clave en la descripción
    for categoria, palabras in palabras_clave.items():
        for palabra in palabras:
            if palabra in descripcion:
                scores[categoria] += 1  # Aumentar el puntaje por cada palabra clave encontrada

    # Devolver la categoría con el puntaje más alto
    max_categoria = max(scores, key=scores.get)
    return max_categoria

# Funcion para dividir un array en 4 y eliminar los sobrantes
def dividir_array(array):
    # Dividimos el array en bloques de 4 elementos
    subarrays = [array[i:i+4] for i in range(0, len(array), 4) if len(array[i:i+4]) == 4]
    return subarrays


# Funcion que elige el idioma dominante
def idiomaDominante(lista_idiomas): 
    for i in lista_idiomas:
        if (i == "Spanish"):
            return "Spanish"
    return "English"

# Funcion para ver si ya esta en el grupo 
def EstaEnGrupo(grupo, cosa):
    for i in grupo:
        if (cosa in i):
            return True
    return False



# Ruta al archivo JSON
data_path = "data/datathon_participants.json"
# Cargar participantes
participants = load_participants(data_path)



# Inicialización de la lista de grupos
Grupos = []
GrupoTemp = []


# codigo 
# Primera condicion
for i in participants: 
    GrupoTemp = []
    GrupoTemp.append(i.id)
    if (not EstaEnGrupo(Grupos,i.id)): 
        for e in participants:
            if (i != e and not EstaEnGrupo(Grupos,e.id)):
                if (idiomaDominante(e.preferred_languages) == idiomaDominante(i.preferred_languages)):
                    if (asignar_cluster(e.objective) == asignar_cluster(i.objective)):
                        if (e.experience_level == i.experience_level):
                            GrupoTemp.append(e.id)
    if (len(GrupoTemp) >= 4):
        array = dividir_array(GrupoTemp)
        for subGrupo in array:
            Grupos.append(subGrupo)

# Segunda condicion
for i in participants:
    GrupoTemp = []
    GrupoTemp.append(i.id)
    if (not EstaEnGrupo(Grupos,i.id)): 
        for e in participants:
            if (i != e and not EstaEnGrupo(Grupos,e.id)):
                if (idiomaDominante(e.preferred_languages) == idiomaDominante(i.preferred_languages)):
                    if (asignar_cluster(e.objective) == asignar_cluster(i.objective)):
                        GrupoTemp.append(e.id)
    if (len(GrupoTemp) >= 4):
        array = dividir_array(GrupoTemp)
        for subGrupo in array:
            Grupos.append(subGrupo)

# Tercera condicion
for i in participants:
    GrupoTemp = []
    GrupoTemp.append(i.id)
    if (not EstaEnGrupo(Grupos,i.id)): 
        for e in participants:
            if (i != e and not EstaEnGrupo(Grupos,e.id)):
                if (idiomaDominante(e.preferred_languages) == idiomaDominante(i.preferred_languages)):
                    GrupoTemp.append(e.id)
    if (len(GrupoTemp) >= 4):
        array = dividir_array(GrupoTemp)
        for subGrupo in array:
            Grupos.append(subGrupo)

# Caso sobrantes 
print(Grupos)  
