#! /bin/python3.10

if __name__ == "__main__":

    alain = {
            "The Nap Master", "The Discount Hunter", "The Time Lord",
            "Remote Control Sleeper", "Alarm Slayer", "aged"
            }
    bernard = {
            "Remote Control Sleeper", "Socks & Sandals", "Early Starter",
            "The Nap Master", "The Tech Skeptic", "aged"
            }
    clotilde = {
            "The No-Filter Speaker", "Alarm Slayer", "The Tech Skeptic",
            "The Discount Hunter", "Socks & Sandals", "aged"
            }

# alain = {
#         'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'
#         }

# bernard = {
#         'first_kill', 'level_10', 'boss_slayer', 'collector'
#           }

# clotilde = {
#         'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
#         'perfectionist'
#            }

    print(" Achievement Tracker System ".center(40, "=") + "\n")

    print(f"Player Alain acheviements: {alain}")
    print(f"Player Bernard acheviements: {bernard}")
    print(f"Player Clotilde acheviements: {clotilde}")

    print("\n" + " Achievement Analytics ".center(40, "="))

    unique = alain.union(bernard)
    unique = unique.union(clotilde)
    print("All unique achievements: ", unique)
    print("Total unique achievements: ", len(unique))

    common = alain.intersection(bernard)
    common = common.intersection(clotilde)
    print("\n" + "Common to all players: ", common)

    rare1 = alain.difference(bernard, clotilde)
    rare2 = bernard.difference(alain, clotilde)
    rare3 = clotilde.difference(alain, bernard)
    rare = rare1.union(rare2)
    rare = rare.union(rare3)
    rare = rare.union(rare1)
    print("Rare achievements (1 player): ", rare)

    duo_common = alain.intersection(bernard)
    print("\n" + "Alain vs Bernard common: ", duo_common)
    unique_alain = alain.difference(bernard)
    print("Alain unique: ", unique_alain)
    unique_bernard = bernard.difference(alain)
    print("Bernard unique: ", unique_bernard)
