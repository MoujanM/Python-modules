# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 16:17:20 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/20 18:58:02 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def game_dashboard():
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    list_data = [('alice', 2300, 'Active'),
                 ('bob', 1800, 'Active'),
                 ('charlie', 2050, 'Active'),
                 ('diana', 2150, 'Off'),
                 ('frank', 800, 'Off')]

    all_data_dict = {'alice':
                     {'score': 2300,
                      'status': 'Active',
                      'region': 'north',
                      'achievements':
                      ['first_blood', 'level_master', 'explorer',
                       'first_blood']},
                     'bob':
                     {'score': 1800,
                      'status': 'Active',
                      'region': 'central',
                      'achievements': ['first_blood', 'explorer']},
                     'charlie':
                     {'score': 2050,
                      'status': 'Active',
                      'region': 'east',
                      'achievements': ['treasure_seeker', 'level_master']},
                     'diana':
                     {'score': 2150,
                      'status': 'Off',
                      'region': 'south',
                      'achievements': ['explorer']},
                     'frank':
                     {'score': 800,
                      'status': 'Off',
                      'region': 'west',
                      'achievements': []}}

    high_scorer = [item[0] for item in list_data if item[1] > 2000]
    double_score = [(item[1] * 2) for item in list_data]
    actives = [item[0] for item in list_data if item[2] == 'Active']
    print(f"High scorers (>2000): {high_scorer}")
    print(f"Scores doubled: {double_score}")
    print(f"Active players: {actives}")

    print("\n=== Dict Comprehension Examples ===")
    player_dict = {item[0]: item[1] for item in list_data}
    mid_scores = [item for item in list_data if 1500 <= item[1] < 2000]
    low_scores = [item for item in list_data if item[1] < 1500]
    score_dict = {"high": len(high_scorer),
                  "medium": len(mid_scores),
                  "low": len(low_scores)}
    achieve_dict = {name: len(data['achievements'])
                    for name, data in all_data_dict.items()}
    print(f"Player scores: {player_dict}")
    print(f"Score categories: {score_dict}")
    print(f"Achievement counts: {achieve_dict}")

    print("\n=== Set Comprehension Examples ===")
    uniques = {name for name in all_data_dict.keys()}
    achieves = {achievement
                for data in all_data_dict.values()
                for achievement in data['achievements']}
    regs = {data['region']
            for data in all_data_dict.values()
            if data['status'] == 'Active'}
    print(f"Unique players: {sorted(uniques)}")
    print(f"Unique achievements: {achieves}")
    print(f"Active regions: {regs}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(all_data_dict.keys())}")
    total_uniques = sum(
        len(set(data['achievements']))
        for data in all_data_dict.values())
    print(f"Total unique achievements: {total_uniques}")
    total_score = sum(data['score']
                      for data in all_data_dict.values())
    print(f"Average score: {total_score / len(all_data_dict.keys())}")
    top_player_name = max(all_data_dict,
                          key=lambda name: all_data_dict[name]['score'])
    top_score = all_data_dict[top_player_name]['score']
    achieve_count = len(all_data_dict[top_player_name]['achievements'])
    print(f"Top performer: {top_player_name} "
          f"({top_score} points, {achieve_count} achievements)")


if __name__ == "__main__":
    game_dashboard()
