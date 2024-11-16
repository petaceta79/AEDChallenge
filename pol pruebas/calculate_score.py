import matplotlib.pyplot as plt
from itertools import groupby
import numpy as np

# Función de puntuación individual
def calculate_score_single(p):
    score = 0

    # Amistad (friend_registration)
    if "friend_registration" in p:
        score += 5000

    # Idioma (preferred_languages)
    if p.get("preferred_languages"):
        score += 500

    # Nivel de experiencia (experience_level)
    if "experience_level" in p:
        score += 400

    # Edad (age)
    if "age" in p:
        score += 300

    # Objetivo (objective)
    if "objective" in p:
        score += 200

    # Universidad (university)
    if "university" in p:
        score += 100

    return score