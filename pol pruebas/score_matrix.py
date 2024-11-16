import numpy as np
from calculate_score import calculate_score

def build_score_matrix(participants):
    n = len(participants)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            score = calculate_score(participants[i], participants[j])
            matrix[i, j] = score
            matrix[j, i] = score
    return matrix
