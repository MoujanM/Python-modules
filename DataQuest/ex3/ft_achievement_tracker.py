# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 16:47:29 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/23 14:51:56 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def achievement_tracker():
    print("=== Achievement Tracker System ===\n")

    achieves = {"alice":
                {'first_kill', 'level_10', 'treasure_hunter',
                 'speed_demon'},
                "bob":
                {'first_kill', 'level_10', 'boss_slayer', 'collector'},
                "charlie":
                {'level_10', 'treasure_hunter', 'boss_slayer',
                 'speed_demon', 'perfectionist'}
                }

    for player in achieves:
        score = achieves[player]
        print(f"Player {player} achievements: {score}")

    print("\n=== Achievement Analytics ===")

    # | equivalent to union()
    uniques = achieves['alice'].union(achieves['bob'], achieves['charlie'])
    print(f"All unique achievements: {uniques}")
    print(f"Total unique achievements: {len(uniques)}", end='\n\n')

    # & equivalent to intersection()
    commons = achieves['alice'] & achieves['bob'] & achieves['charlie']
    print(f"Common to all players: {commons}")

    # ^ equivalent to symmetric_difference()
    rares = (achieves['charlie'] ^ achieves['alice']
             ^ achieves['bob']) - commons
    print(f"Rare achievements (1 player): {rares}", end='\n\n')

    ab_common = achieves['alice'] & achieves['bob']
    print(f"Alice vs Bob common: {ab_common}")
    print(f"Alice unique: {achieves['alice'] - ab_common}")
    print(f"Bob unique: {achieves['bob'] - ab_common}")


if __name__ == "__main__":
    achievement_tracker()
