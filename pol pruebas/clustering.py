from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform
import numpy as np

def cluster_participants(score_matrix, participants, max_group_size=4):
    # Convertir la matriz de puntuación en distancias
    distances = 1 / (1 + score_matrix)

    # Asegurarse de que no haya distancias inválidas (NaN o infinitas)
    distances = np.nan_to_num(distances, nan=0.0, posinf=1.0, neginf=1.0)

    # Asegurarse de que la diagonal sea cero
    np.fill_diagonal(distances, 0)

    # Convertir la matriz de distancias en un vector unidimensional (formato condensado)
    condensed_distances = distances[np.triu_indices_from(distances, k=1)]

    # Realizar el clustering jerárquico
    linked = linkage(condensed_distances, method='average')

    # Generar los clusters iniciales con un número adecuado de clusters
    num_clusters = len(participants) // max_group_size + 1  # Asegurarse de tener suficientes grupos
    initial_clusters = fcluster(linked, t=num_clusters, criterion='maxclust')

    # Organizar los participantes en un diccionario de grupos
    groups = {}
    for i, cluster_id in enumerate(initial_clusters):
        if cluster_id not in groups:
            groups[cluster_id] = []
        groups[cluster_id].append((participants[i], score_matrix[i]))

    # Asignar los participantes a los grupos con la mayor puntuación
    final_groups = []
    assigned_participants = set()  # Para rastrear los participantes asignados

    for cluster_id, group in groups.items():
        # Ordenar los participantes dentro del grupo según la puntuación
        group_sorted = sorted(group, key=lambda x: sum(x[1]), reverse=True)
        
        group_copy = []  # Para almacenar el grupo final
        for participant, _ in group_sorted:
            if participant['id'] not in assigned_participants:
                group_copy.append(participant)
                assigned_participants.add(participant['id'])

            # Limitar al tamaño máximo del grupo
            if len(group_copy) >= max_group_size:
                break

        # Añadir el grupo al resultado final
        if group_copy:
            final_groups.append(group_copy)

    # Si hay menos grupos de lo necesario, distribuir los participantes restantes
    all_participants = set([p['id'] for p in participants])
    remaining_participants = all_participants - assigned_participants

    # Asignar los participantes restantes a los grupos existentes
    for participant_id in remaining_participants:
        for group in final_groups:
            if len(group) < max_group_size:
                group.append(next(p for p in participants if p['id'] == participant_id))
                assigned_participants.add(participant_id)
                break

    return final_groups




