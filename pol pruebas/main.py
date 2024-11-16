from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import linkage, fcluster
from load_participants import load_participants
from score_matrix import build_score_matrix
from clustering import cluster_participants

def main():
    # Cargar participantes
    participants = load_participants("participants.json")

    # Crear matriz de puntuación
    score_matrix = build_score_matrix(participants)

    # Convertir la matriz de puntuación en distancias
    distances = 1 / (1 + score_matrix)
    condensed_distances = squareform(distances)

    # Realizar clustering jerárquico
    linked = linkage(condensed_distances, method='average')

    # Generar grupos respetando el tamaño máximo
    groups = cluster_participants(score_matrix, participants)

    # Mostrar resultados
    for i, group in enumerate(groups, 1):
        print(f"Grupo {i}:")
        for member in group:
            print(f"  - {member['name']}")
        print()

if __name__ == "__main__":
    main()
