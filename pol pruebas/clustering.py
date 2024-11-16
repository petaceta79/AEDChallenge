from scipy.cluster.hierarchy import linkage, fcluster

def cluster_participants(score_matrix, participants, max_group_size=4):
    # Convertimos la matriz de puntuación en distancias inversas (mayor puntuación = menor distancia)
    distances = 1 / (1 + score_matrix)

    # Realizamos el agrupamiento jerárquico
    linked = linkage(distances, method='average')

    # Generamos los clusters con una restricción inicial (agrupamiento flexible)
    initial_clusters = fcluster(linked, t=max_group_size, criterion='maxclust')

    # Validamos grupos para cumplir el tamaño máximo permitido
    groups = {}
    for i, cluster_id in enumerate(initial_clusters):
        groups.setdefault(cluster_id, []).append(participants[i])

    # Ajustamos para asegurar máximo 4 personas por grupo
    final_groups = []
    for group in groups.values():
        while len(group) > max_group_size:
            final_groups.append(group[:max_group_size])
            group = group[max_group_size:]
        if group:
            final_groups.append(group)

    return final_groups
