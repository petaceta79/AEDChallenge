def calculate_score(p1, p2):
    score = 0

    # Amistad (friend_registration)
    if p1["id"] in p2.get("friend_registration", []) or p2["id"] in p1.get("friend_registration", []):
        score += 5000

    # Idioma (preferred_languages)
    common_languages = set(p1["preferred_languages"]) & set(p2["preferred_languages"])
    if common_languages:
        score += 500

    # Nivel de experiencia (experience_level)
    if p1["experience_level"] == p2["experience_level"]:
        score += 400

    # Edad (age)
    if p1["age"] == p2["age"]:
        score += 300

    # Objetivo (objective)
    if p1["objective"] == p2["objective"]:
        score += 200

    # Universidad (university)
    if p1["university"] == p2["university"]:
        score += 100

    return score
