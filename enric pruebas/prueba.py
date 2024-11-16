import json
import uuid
import random
from dataclasses import dataclass
from typing import List, Dict, Union
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from itertools import combinations

@dataclass
class Participant:
    id: uuid.UUID
    name: str
    email: str
    age: int
    year_of_study: str
    university: str
    dietary_restrictions: str
    programming_skills: Dict[str, int]
    experience_level: str
    hackathons_done: int
    interests: List[str]
    preferred_role: str
    objective: str
    preferred_languages: List[str]
    friend_registration: List[uuid.UUID]
    preferred_team_size: int
    availability: Dict[str, bool]


def load_participants(file_path: str) -> List[Participant]:
    with open(file_path, "r") as file:
        data = json.load(file)
    return [Participant(**participant) for participant in data]


def calculate_compatibility(p1: Participant, p2: Participant) -> float:
    """
    Calculate compatibility score between two participants.
    """
    score = 0

    # Friends: High priority
    if p2.id in p1.friend_registration or p1.id in p2.friend_registration:
        score += 30

    # Programming Languages
    common_languages = set(p1.preferred_languages).intersection(p2.preferred_languages)
    score += len(common_languages) * 10

    # Experience Level
    levels = ["Beginner", "Intermediate", "Advanced"]
    exp_diff = abs(levels.index(p1.experience_level) - levels.index(p2.experience_level))
    score += max(10 - (exp_diff * 5), 0)

    # Objectives
    if p1.objective == p2.objective:
        score += 15

    # Interests
    common_interests = set(p1.interests).intersection(p2.interests)
    score += len(common_interests) * 5

    return score


def form_teams(participants: List[Participant], max_team_size: int = 4) -> List[List[Participant]]:
    """
    Form teams of participants based on compatibility scores.
    """
    # Calculate all pairwise scores
    pair_scores = {
        (p1.id, p2.id): calculate_compatibility(p1, p2)
        for p1, p2 in combinations(participants, 2)
    }

    # Sort participants by compatibility score
    participants = sorted(participants, key=lambda p: sum(pair_scores.get((p.id, other.id), 0) for other in participants), reverse=True)

    teams = []
    used = set()

    for participant in participants:
        if participant.id in used:
            continue

        # Find the most compatible team
        team = [participant]
        for other in participants:
            if other.id not in used and other.id != participant.id:
                if len(team) < max_team_size:
                    team.append(other)
                    used.add(other.id)
        teams.append(team)

    return teams


def visualize_teams(teams: List[List[Participant]]) -> None:
    """
    Create visualizations of team compositions.
    """
    # Bar chart for team sizes
    team_sizes = [len(team) for team in teams]
    plt.bar(range(1, len(teams) + 1), team_sizes, color='skyblue')
    plt.xlabel("Team Number")
    plt.ylabel("Team Size")
    plt.title("Team Sizes")
    plt.show()

    # Network graph for relationships
    import networkx as nx
    G = nx.Graph()

    for team in teams:
        for participant in team:
            G.add_node(participant.name)
        for p1, p2 in combinations(team, 2):
            G.add_edge(p1.name, p2.name)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", font_size=10, font_weight="bold")
    plt.show()


if __name__ == "__main__":
    # Load participants
    participants = load_participants("data/datathon_participants.json")

    # Form teams
    teams = form_teams(participants)

    # Display teams
    for i, team in enumerate(teams):
        print(f"\nTeam {i + 1}:")
        for member in team:
            print(f"  - {member.name} ({member.objective})")

    # Visualize teams
    visualize_teams(teams)
