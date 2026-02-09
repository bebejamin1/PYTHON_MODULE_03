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

    print("High scorers (>2000): ", end="")
    print(*high_score, sep=" | ")
    print("Scores doubled: ", end="")
    print(*doubled_score, sep=" | ")
    print("Active players: ", end="")
    print(*players_active, sep=" | ")


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

    print("Player scores: ", end="")
    print(*player_score, sep=" | ")
    print("Score categories: ", end="")
    print(*categories_score, sep=" | ")
    print("Achievement counts: ", end="")
    print(*achivement_count, sep=" | ")


# =============================================================================
# ======================== Set Comprehension Examples =========================
# =============================================================================


def exemple_set() -> int:

    unique_player = {player["name"] for player in Players}

    unique_achi = {achievement for player in Players
                   for achievement in player["achievement"]}

    region = {player["region"] for player in Players}

    print("Unique players: ", end="")
    print(*unique_player, sep=" | ")
    print("Unique achievements: ", end="")
    print(*unique_achi, sep=" | ")
    print("Active regions: ", end="")
    print(*region, sep=" | ")


# =============================================================================
# ============================ Combined Analysis ==============================
# =============================================================================


def combined_analysis() -> None:

    total_player = [player["name"] for player in Players]

    score_list = [player["score"] for player in Players]

    length = len({achievement for player in Players for achievement
                  in player["achievement"]})

    best_p = [dict(player) for player in Players
              if player["score"] == max(score_list)]

    print("Total players: ", len(total_player))
    print("Total unique achievements: ", length)
    print(f"Average score: {(sum(score_list) / len(score_list)):.1f}")
    print("Top performer: ", end="")
    print(f"{best_p[0]['name']} ({best_p[0]['score']} points, "
          f"{len(best_p[0]['achievement'])} achievements)")


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
