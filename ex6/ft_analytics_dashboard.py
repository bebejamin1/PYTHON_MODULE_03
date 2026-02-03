#! /bin/python3.10

import random


# =============================================================================
# ================================= DATA ======================================
# =============================================================================


achievement_data = [
    "TaxPayer",  # 0
    "Pyromaniac",  # 1
    "Tunnel Vision",  # 2
    "Feat Fanatic",  # 3
    "bbeaurai storm",  # 4
    "BlackPink",  # 5
    "Double S",  # 6
    "Nothing personal",  # 7
    "I'm On A Boat",  # 8
    "END_GAME_WIN",  # 9
    "Unique",  # 10
]

Elouann = {
    "name": "Elouann",
    "score": random.randint(20, 8000),
    "achievement": [
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                    ],
    "region": "north"
}

Hugo = {
    "name": "Hugo",
    "score": random.randint(20, 8000),
    "achievement": [
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                   achievement_data[10],
                    ],
    "region": "east"
}

Fleur = {
    "name": "Fleur",
    "score": random.randint(20, 8000),
    "achievement": [
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                    ],
    "region": "far east"
}

Timothee = {
    "name": "Timothee",
    "score": random.randint(20, 8000),
    "achievement": [
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                    ],
    "region": "central"
}

Valerie = {
    "name": "Valerie",
    "score": random.randint(20, 8000),
    "achievement": [
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                    ],
    "region": "south"
}

NomiNoe = {
    "name": "NomiNoe",
    "score": random.randint(20, 8000),
    "achievement": [
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                   achievement_data[random.randint(0, 9)],
                    ],
    "region": "west"
}

Players = [Elouann, Hugo, Fleur, Timothee, Valerie, NomiNoe]


# =============================================================================
# ======================= List Comprehension Examples =========================
# =============================================================================


def exemple_list() -> None:

    high_score = sorted([player["name"] for player in Players
                        if player["score"] > 2000])

    doubled_score = [player["score"] * 2 for player in Players]

    players_active = [player["name"] for player in Players
                      if len(player["achievement"]) > 3]

    print("High scorers (>2000): ", high_score)
    print("Scores doubled: ", doubled_score)
    print("Active players: ", players_active)


# =============================================================================
# ======================= Dict Comprehension Examples =========================
# =============================================================================


def score_cate_int(score: int) -> int:
    if (score < 2000):
        return (1)
    if (score >= 2000 and score < 5000):
        return (2)
    if (score >= 5000):
        return (3)


def score_cate_str(score: int) -> str:
    if (score < 2000):
        return ("low")
    if (score >= 2000 and score < 5000):
        return ("medium")
    if (score >= 5000):
        return ("high")


def exemple_dict() -> None:

    player_score = {player["name"]: player["score"] for player in Players}

    categories_score = {score_cate_str(score): score_cate_int(score)
                        for score in player_score.values()}

    achivement_count = {player["name"]: len(player["achievement"])
                        for player in Players}

    print("Player scores: ", player_score)
    print("Score categories: ", categories_score)
    print("Achievement counts: ", achivement_count)


# =============================================================================
# ======================== Set Comprehension Examples =========================
# =============================================================================


def exemple_set() -> int:
    data = set(achievement_data)

    unique_player = {player["name"] for player in Players}

    unique_achievements = set()
    for player in Players:
        unique_achievements = data.intersection(player["achievement"])

    unique_achi = {data.intersection(player["achievement"])
                   for player in Players}

    region = {player["region"] for player in Players}

    print("Unique players: ", unique_player)
    print("Unique achievements: ", unique_achi)
    print("Unique achievements 2: ", unique_achievements)
    print("Active regions: ", region)
    return (len(unique_achi))


# =============================================================================
# ============================ Combined Analysis ==============================
# =============================================================================


def best_player() -> int:
    stock_best_score = 0
    for player in Players:
        if (stock_best_score < player["score"]):
            stock_best_score = player["score"]
    return (stock_best_score)


def combined_analysis() -> None:
    count = 0
    for der in Players:
        count += 1

    data = set(achievement_data)
    tt_achievements = set()
    for player in Players:
        tt_achievements = data.intersection(player["achievement"])
    length = len(tt_achievements)

    sum = 0
    for player in Players:
        sum += player["score"]
    average = (sum / count)

    print("Total players: ", count)
    print("Total unique achievements: ", length)
    print(f"Average score: {average:.1f}")
    print("Top performer: ", end="")
    best_score = best_player()
    for p in Players:
        if (p["score"] == best_score):
            print(f"{p['name']} ({p['score']} points, {len(p['achievement'])}"
                  " achievements)")


# =============================================================================
# =============================== TESTER ======================================
# =============================================================================


def ft_analytics_dashboard() -> None:
    print(" List Comprehension Examples ".center(79, "="))
    exemple_list()

    print("\n" + " Dict Comprehension Examples ".center(79, "="))
    exemple_dict()

    print("\n" + " Set Comprehension Examples ".center(79, "="))
    exemple_set()

    print("\n" + " Combined Analysis ".center(79, "="))
    combined_analysis()


if __name__ == "__main__":
    print(" Game Analytics Dashboard ".center(79, "="))
    print("".center(79, "="))
    ft_analytics_dashboard()
