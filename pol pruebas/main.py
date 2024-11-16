from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import linkage, fcluster
from load_participants import load_participants
from score_matrix import build_score_matrix
from clustering import cluster_participants

def main():
    # Cargar participantes
    participants = load_participants("datathon_participants.json")

    # Crear matriz de puntuación
    score_matrix = build_score_matrix(participants)

    # Agrupar participantes
    groups = cluster_participants(score_matrix, participants)

    # Mostrar resultados
    for i, group in enumerate(groups, 1):
        print(f"Grupo {i}:")
        for member in group:
            print(f"  - {member['name']}")
        print()

if __name__ == "__main__":
    main()
