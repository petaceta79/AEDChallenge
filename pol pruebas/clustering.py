from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform
import numpy as np

def cluster_participants(score_matrix, participants, max_group_size=4):
    # Revisar la matriz de puntuaciones
    print("Matriz de puntuaciones:")
    print(score_matrix)

    # Convertir la matriz de puntuación en distancias
    distances = 1 / (1 + score_matrix)

    # Asegurarse de que no haya distancias inválidas (NaN o infinitas)
    distances = np.nan_to_num(distances, nan=0.0, posinf=1.0, neginf=1.0)

    # Asegurarse de que la diagonal sea cero
    np.fill_diagonal(distances, 0)

    # Verificar la matriz de distancias antes de squareform
    print("Matriz de distancias antes de squareform:")
    print(distances)

    # Convertir la matriz de distancias en un vector unidimensional (formato condensado)
    try:
        condensed_distances = distances[np.triu_indices_from(distances, k=1)]
        print("Condensed distances:")
        print(condensed_distances)
    except Exception as e:
        print("Error al convertir la matriz de distancias en formato condensado.")
        print("Detalles del error:", e)
        return []

    # Realizar el clustering jerárquico
    linked = linkage(condensed_distances, method='average')

    # Generar los clusters iniciales
    initial_clusters = fcluster(linked, t=max_group_size, criterion='maxclust')

    # Organizar participantes en grupos
    groups = {}
    assigned_participants = set()  # Conjunto para seguir el registro de participantes asignados

    for i, cluster_id in enumerate(initial_clusters):
        if participants[i]['id'] not in assigned_participants:
            # Si el participante no ha sido asignado, lo añadimos al grupo
            groups.setdefault(cluster_id, []).append(participants[i])
            assigned_participants.add(participants[i]['id'])  # Marcamos al participante como asignado

    # Ajustar los grupos al tamaño máximo permitido
    final_groups = []
    for group in groups.values():
        while len(group) > max_group_size:
            final_groups.append(group[:max_group_size])
            group = group[max_group_size:]
        if group:
            final_groups.append(group)

    return final_groups



