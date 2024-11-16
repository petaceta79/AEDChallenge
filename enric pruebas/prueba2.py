import json

# Diccionario con las palabras clave para cada grupo
palabras_clave = {
    "WIN": ["top", "win", "first", "trophy", "winning", "competitive"],
    "FRIENDS": ["friends", "meet", "new", "people", "connections", "social"],
    "LEARN": ["learn", "try", "abilities", "skills", "growth", "learning", "code"]
}

# Ruta del archivo JSON
data_path = "data/datathon_participants.json"

# Función para detectar el grupo de palabras clave en una descripción
def asignar_cluster(descripcion, palabras_clave):
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

# Cargar los participantes desde el archivo JSON
with open(data_path, "r", encoding="utf-8") as file:
    participantes = json.load(file)

# Función para obtener el grupo de un solo participante
def obtener_objetivo_participante(nombre_participante):
    # Buscar el participante por nombre
    for participante in participantes:
        if participante.get('name') == nombre_participante:
            # Verificamos si 'objective' está en los datos del participante
            if 'objective' in participante and participante['objective'].strip():  # Verificamos que la descripción no esté vacía
                descripcion = participante['objective']
                categoria_asignada = asignar_cluster(descripcion, palabras_clave)
                return f"El objetivo de {nombre_participante} es: {categoria_asignada}"
    return f"No se encontró un participante con el nombre: {nombre_participante}"

# Ejemplo de cómo usar la función
nombre_participante = input()  # Cambia por el nombre del participante que quieres consultar
resultado = obtener_objetivo_participante(nombre_participante)
print(resultado)
