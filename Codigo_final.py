from rich import print
from participant import load_participants



# Funciones 

# Dado el id devuele el objeto
def get_person_by_id(participants, id):
    for participant in participants:
        if participant.id == id:
            return participant
    return None  # Devuelve None si no encuentra el ID

# Devuelve false en caso que su rol este ya repetido 
def repe_rol(GrupoTemp, rol, participants):
    for i in GrupoTemp:
        if (get_person_by_id(participants, i).preferred_role == rol):
            return False
    return True


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

def ChangeIdName(personas, id):
    for persona in personas:
        if persona.id == id:  # Acceso al atributo en lugar de clave de diccionario
            return persona.name
    return None  # Devuelve None si no se encuentra el id
    
# Funcion para dividir un array en 4 y eliminar los sobrantes
def dividir_array(array):
    # Dividimos el array en bloques de 4 elementos
    subarrays = [array[i:i+4] for i in range(0, len(array), 4) if len(array[i:i+4]) == 4]
    return subarrays


# Funcion que elige el idioma dominante
def idiomaDominante(lista_idiomas): 
    for i in lista_idiomas:
        if (i == "Catalan"):
            return "Catalan"
        elif (i == "Spanish"):
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

# Todas condicion
for i in participants: 
    GrupoTemp = []
    GrupoTemp.append(i.id)
    if (not EstaEnGrupo(Grupos,i.id)): 
        for e in participants:
            if (i != e and not EstaEnGrupo(Grupos,e.id)):
                if (idiomaDominante(e.preferred_languages) == idiomaDominante(i.preferred_languages)):
                    if (asignar_cluster(e.objective) == asignar_cluster(i.objective)):
                        if (repe_rol(GrupoTemp, e.preferred_role, participants)):
                            if (e.experience_level == i.experience_level):
                                if (i.age > (e.age - 1) and i.age < (e.age + 1)):
                                    GrupoTemp.append(e.id)
    if (len(GrupoTemp) >= 4):
        array = dividir_array(GrupoTemp)
        for subGrupo in array:
            Grupos.append(subGrupo)

# 1r condicion
for i in participants: 
    GrupoTemp = []
    GrupoTemp.append(i.id)
    if (not EstaEnGrupo(Grupos,i.id)): 
        for e in participants:
            if (i != e and not EstaEnGrupo(Grupos,e.id)):
                if (idiomaDominante(e.preferred_languages) == idiomaDominante(i.preferred_languages)):
                    if (asignar_cluster(e.objective) == asignar_cluster(i.objective)):
                        if (repe_rol(GrupoTemp, e.preferred_role, participants)):
                            if (e.experience_level == i.experience_level):
                                GrupoTemp.append(e.id)
    if (len(GrupoTemp) >= 4):
        array = dividir_array(GrupoTemp)
        for subGrupo in array:
            Grupos.append(subGrupo)

# 2nd condicion
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

# 3r condicion
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

# 4t condicion
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
GrupoTemp = []
for i in participants:
    if (not EstaEnGrupo(Grupos,i.id)): 
        GrupoTemp.append(i.id)
if (len(GrupoTemp) >= 4):
        array = dividir_array(GrupoTemp)
        for subGrupo in array:
            Grupos.append(subGrupo)




# Ejemplo para visualizar los resultados
# Crear array con los nombres 
GruposNombres = []

for i in Grupos:
    array = []
    for e in i:  # Supongo que quieres iterar sobre los elementos de cada grupo en 'Grupos'
        array.append(ChangeIdName(participants, e))
    GruposNombres.append(array)

print(GruposNombres)